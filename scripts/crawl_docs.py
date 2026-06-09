#!/usr/bin/env python3
"""
Tushare 官方文档自动爬取与同步工具

功能：
  1. 用 Playwright 无头浏览器从 tushare.pro/document/2 爬取最新 API 文档
  2. 对比本地已有文档，检测新增和变更
  3. 自动更新 reference/接口文档/ 下的 Markdown 文件
  4. 重新生成 reference/all_links.json 和 reference/README.md
  5. 输出变更报告（支持 GitHub Actions GITHUB_OUTPUT）

使用：
  python scripts/crawl_docs.py                 # 完整同步
  python scripts/crawl_docs.py --dry-run       # 只检测，不写入
  python scripts/crawl_docs.py --doc-id 25     # 只爬指定文档
  python scripts/crawl_docs.py --max-docs 5    # 限制数量（测试用）

依赖：
  pip install playwright beautifulsoup4 markdownify
  playwright install chromium
"""

import argparse
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from bs4 import BeautifulSoup, Tag

try:
    from markdownify import MarkdownConverter
except ImportError:
    MarkdownConverter = None

try:
    from playwright.sync_api import sync_playwright, Browser, Page
except ImportError:
    print("错误: 需要安装 playwright")
    print("  pip install playwright")
    print("  playwright install chromium")
    sys.exit(1)

try:
    import ddddocr
except ImportError:
    ddddocr = None

import requests as http_requests

# ---------------------------------------------------------------------------
# 路径常量
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = PROJECT_ROOT / "reference" / "接口文档"
LINKS_FILE = PROJECT_ROOT / "reference" / "all_links.json"
README_FILE = PROJECT_ROOT / "reference" / "README.md"
HASH_FILE = PROJECT_ROOT / "reference" / ".content_hashes.json"

# ---------------------------------------------------------------------------
# 网络常量
# ---------------------------------------------------------------------------
BASE_URL = "https://tushare.pro/document/2"
INDEX_URL = BASE_URL
PAGE_LOAD_TIMEOUT = 30000  # ms
NAVIGATION_TIMEOUT = 20000  # ms

# ---------------------------------------------------------------------------
# 已知的分类标题 doc_id（导航树中的分类节点，不是具体接口文档）
# ---------------------------------------------------------------------------
CATEGORY_DOC_IDS = {
    "14", "24", "15", "16", "17", "291", "330", "342", "346",
    "384", "93", "18", "134", "283", "157", "184", "177", "190",
    "251", "82", "83", "147", "224", "225", "226", "240", "241",
    "309", "324", "217", "142", "263", "148", "218",
}

# ---------------------------------------------------------------------------
# 分类关键词映射（用于 README.md 索引自动分类）
# ---------------------------------------------------------------------------
CATEGORY_KEYWORDS: List[Tuple[str, List[str]]] = [
    ("ETF专题", ["ETF"]),
    ("指数专题", ["指数", "申万", "中信", "大盘指数"]),
    ("公募基金", ["基金"]),
    ("期货数据", ["期货", "合约信息", "仓单日报", "持仓排名", "南华", "结算参数", "主力与连续", "涨跌停价格"]),
    ("现货数据", ["黄金", "现货"]),
    ("期权数据", ["期权"]),
    ("债券专题", ["可转债", "债券", "国债", "柜台流通", "大宗交易", "债券回购"]),
    ("外汇数据", ["外汇"]),
    ("港股数据", ["港股"]),
    ("美股数据", ["美股"]),
    ("宏观经济", ["GDP", "CPI", "PPI", "PMI", "Shibor", "LPR", "Libor", "Hibor", "利率", "货币供应", "社融", "宏观"]),
    ("大模型语料", ["新闻", "公告", "互动", "政策库", "研究报告"]),
    ("行业经济", ["电影", "票房", "电视剧", "台湾", "基金销售", "保有规模"]),
    ("股票数据", ["股票", "龙虎榜", "涨跌停", "连板", "游资", "筹码", "竞价", "融资融券",
                "转融", "股东", "股权质押", "限售股", "资金流向",
                "沪深港通", "沪深股通", "港股通", "停复牌", "业绩", "分红",
                "财务", "主营", "前十大", "机构调研", "盈利预测", "金股",
                "技术面", "九转", "比价"]),
]


# =========================================================================
# 工具函数
# =========================================================================

def content_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sanitize_filename(name: str) -> str:
    name = re.sub(r'[<>:"/\\|?*]', '_', name)
    name = name.replace('/', '_').replace('\\', '_')
    return name.strip('. ')


def load_json(path: Path, default=None):
    if path.exists():
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return default if default is not None else {}


def save_json(path: Path, data, indent=2):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


# =========================================================================
# HTML → Markdown 转换
# =========================================================================

class TushareDocConverter:
    """将 Tushare 文档页面的 HTML 内容转为 Markdown"""

    def convert(self, html: str) -> str:
        soup = BeautifulSoup(html, "html.parser")
        content_el = self._find_content(soup)
        if content_el is None:
            return ""
        return self._to_markdown(content_el)

    def _find_content(self, soup: BeautifulSoup) -> Optional[Tag]:
        # 按优先级尝试多种选择器
        selectors = [
            "div.tui-editor-contents",
            "div.te-preview",
            "div.markdown-body",
            "div#document-content",
            "div.doc-content",
            "article",
        ]
        for sel in selectors:
            el = soup.select_one(sel)
            if el and len(el.get_text(strip=True)) > 50:
                return el

        # 兜底：找文本量最大的 div
        best, best_len = None, 0
        for div in soup.find_all("div"):
            tl = len(div.get_text(strip=True))
            if tl > best_len:
                best_len, best = tl, div
        return best if best_len > 100 else None

    def _to_markdown(self, el: Tag) -> str:
        if MarkdownConverter is not None:
            converter = MarkdownConverter(
                heading_style="ATX", bullets="-", code_language="", strip=["img"],
            )
            md_text = converter.convert_soup(el)
        else:
            md_text = self._fallback_convert(el)
        return self._clean(md_text)

    def _fallback_convert(self, el: Tag) -> str:
        parts: List[str] = []
        self._walk(el, parts)
        return "\n".join(parts)

    def _walk(self, el: Tag, parts: List[str]):
        for child in el.children:
            if isinstance(child, str):
                text = child.strip()
                if text:
                    parts.append(text)
                continue
            if not isinstance(child, Tag):
                continue
            tag = child.name
            if tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
                parts.append(f"\n{'#' * int(tag[1])} {child.get_text(strip=True)}\n")
            elif tag == "table":
                parts.append(self._table_to_md(child))
            elif tag == "pre":
                parts.append(f"\n```\n{child.get_text()}\n```\n")
            elif tag == "hr":
                parts.append("\n---\n")
            elif tag in ("strong", "b"):
                parts.append(f"**{child.get_text(strip=True)}**")
            elif tag in ("em", "i"):
                parts.append(f"*{child.get_text(strip=True)}*")
            elif tag == "br":
                parts.append("\n")
            elif tag in ("ul", "ol"):
                for li in child.find_all("li", recursive=False):
                    parts.append(f"- {li.get_text(strip=True)}")
            elif tag == "img":
                pass
            else:
                self._walk(child, parts)

    def _table_to_md(self, table: Tag) -> str:
        rows: List[List[str]] = []
        for tr in table.find_all("tr"):
            cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
            if cells:
                rows.append(cells)
        if not rows:
            return ""
        ncols = len(rows[0])
        lines = ["| " + " | ".join(rows[0]) + " |"]
        lines.append("| " + " | ".join(["---"] * ncols) + " |")
        for row in rows[1:]:
            while len(row) < ncols:
                row.append("")
            lines.append("| " + " | ".join(row[:ncols]) + " |")
        return "\n".join(lines)

    @staticmethod
    def _clean(text: str) -> str:
        text = re.sub(r"\n{4,}", "\n\n\n", text)
        for entity, char in [("&nbsp;", " "), ("&amp;", "&"), ("&lt;", "<"), ("&gt;", ">")]:
            text = text.replace(entity, char)
        return text.strip()


# =========================================================================
# Playwright 爬取器
# =========================================================================

class TushareDocCrawler:
    """使用 Playwright 无头浏览器爬取 Tushare 文档"""

    def __init__(self, verbose: bool = False,
                 account: Optional[str] = None,
                 password: Optional[str] = None):
        self.converter = TushareDocConverter()
        self.verbose = verbose
        self.account = account
        self.password = password
        self._pw = None
        self._browser: Optional[Browser] = None
        self._page: Optional[Page] = None
        self._logged_in = False

    # ---- 生命周期 ----

    def start(self):
        self._pw = sync_playwright().start()
        self._browser = self._pw.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-gpu"],
        )
        self._page = self._browser.new_page()
        self._page.set_default_timeout(PAGE_LOAD_TIMEOUT)
        self._log("Playwright 浏览器已启动")

        # Try login if credentials are provided
        if self.account and self.password:
            self._login()
        else:
            print("  未提供登录凭据，尝试无登录访问...")

    def _login(self):
        """Log in to Tushare via the REST API with CAPTCHA OCR."""
        print("  正在登录 Tushare (API 方式)...")
        try:
            api_base = "https://tushare.pro/wctapi"
            http_headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Content-Type": "application/json",
                "Referer": "https://tushare.pro/weborder/",
                "Origin": "https://tushare.pro",
            }

            # Step 1: Get CAPTCHA
            captcha_resp = http_requests.get(
                f"{api_base}/user/login/captcha", headers=http_headers, timeout=15
            )
            captcha_data = captcha_resp.json().get("data", {})
            captcha_id = captcha_data.get("captcha_id", "")
            captcha_image_b64 = captcha_data.get("image", "")

            if not captcha_id:
                print("  获取验证码失败")
                return

            self._log(f"  获取验证码: captcha_id={captcha_id[:12]}...")

            # Step 2: OCR the CAPTCHA
            captcha_text = self._ocr_captcha(captcha_image_b64)
            if not captcha_text:
                print("  验证码识别失败")
                return
            self._log(f"  验证码识别结果: {captcha_text}")

            # Step 3: Login via API
            login_data = {
                "username": self.account,
                "password": self.password,
                "captcha_id": captcha_id,
                "captcha": captcha_text,
            }
            login_resp = http_requests.post(
                f"{api_base}/user/login/password",
                json=login_data,
                headers=http_headers,
                timeout=15,
            )
            login_result = login_resp.json()
            login_code = login_result.get("code", -1)
            login_msg = login_result.get("message", "")

            if login_code != 0:
                print(f"  登录失败: [{login_code}] {login_msg}")
                if "captcha" in login_msg.lower() or "验证码" in login_msg:
                    print("  提示: 验证码错误，将重试...")
                    # Retry once
                    time.sleep(1)
                    captcha_resp2 = http_requests.get(
                        f"{api_base}/user/login/captcha", headers=http_headers, timeout=15
                    )
                    cd2 = captcha_resp2.json().get("data", {})
                    cid2 = cd2.get("captcha_id", "")
                    ci2 = cd2.get("image", "")
                    ct2 = self._ocr_captcha(ci2)
                    if ct2:
                        login_data["captcha_id"] = cid2
                        login_data["captcha"] = ct2
                        login_resp2 = http_requests.post(
                            f"{api_base}/user/login/password",
                            json=login_data,
                            headers=http_headers,
                            timeout=15,
                        )
                        lr2 = login_resp2.json()
                        if lr2.get("code", -1) != 0:
                            print(f"  重试登录仍失败: [{lr2.get('code')}] {lr2.get('message')}")
                            return
                        login_result = lr2
                        login_resp = login_resp2
                else:
                    return

            # Step 4: Extract cookies and apply to Playwright
            print("  API 登录成功，同步 cookies 到浏览器...")
            cookies = http_requests.utils.dict_from_cookiejar(login_resp.cookies)

            # Also set cookies via cookie header on Playwright page
            for name, value in cookies.items():
                self._page.context.add_cookies([{
                    "name": name,
                    "value": value,
                    "domain": "tushare.pro",
                    "path": "/",
                }])

            # Verify login by navigating to a doc page
            self._page.goto(f"{BASE_URL}?doc_id=25", wait_until="networkidle", timeout=PAGE_LOAD_TIMEOUT)
            time.sleep(2)

            # Check if login iframe still shows
            for frame in self._page.frames:
                if "weborder" in frame.url and "login" in frame.url:
                    print("  Cookie 未生效（仍在登录页面），尝试刷新...")
                    self._page.reload(wait_until="networkidle", timeout=PAGE_LOAD_TIMEOUT)
                    time.sleep(2)
                    break

            # Final check
            body_text = self._page.text_content("body") or ""
            if "接口" in body_text:
                self._logged_in = True
                print("  登录成功！文档内容可访问")
            else:
                # Still might work - some docs load differently
                still_login = any(
                    "weborder" in f.url and "login" in f.url
                    for f in self._page.frames
                )
                if not still_login:
                    self._logged_in = True
                    print("  登录可能成功（页面已离开登录界面）")
                else:
                    print("  登录最终失败")

        except Exception as e:
            print(f"  登录过程出错: {e}")
            self._logged_in = False

    def _ocr_captcha(self, image_b64: str) -> str:
        """OCR a base64-encoded CAPTCHA image."""
        if not image_b64:
            return ""
        try:
            if ddddocr is not None:
                # Use ddddocr for CAPTCHA recognition
                ocr = ddddocr.DdddOcr(show_ad=False)
                # Remove data URL prefix if present
                if "," in image_b64:
                    image_b64 = image_b64.split(",", 1)[1]
                import base64
                image_bytes = base64.b64decode(image_b64)
                result = ocr.classification(image_bytes)
                return result.strip()
            else:
                self._log("  ddddocr 未安装，跳过验证码识别")
                return ""
        except Exception as e:
            self._log(f"  OCR 错误: {e}")
            return ""

    def _ensure_logged_in(self) -> bool:
        """Check if we need to log in and do so if needed."""
        if self._logged_in:
            return True
        if self.account and self.password:
            self._login()
        return self._logged_in

    def close(self):
        if self._browser:
            self._browser.close()
        if self._pw:
            self._pw.stop()
        self._log("Playwright 浏览器已关闭")

    # ---- 发现文档列表 ----

    def discover_docs(self) -> List[Dict]:
        """从索引页导航树发现所有文档 doc_id 和名称"""
        self._log("正在加载索引页发现文档列表...")
        self._page.goto(INDEX_URL, wait_until="networkidle", timeout=PAGE_LOAD_TIMEOUT)
        time.sleep(2)  # 等待 jstree 渲染完成

        docs: List[Dict] = []
        seen: set = set()

        # 从 jstree 导航中提取链接
        links = self._page.query_selector_all("a.jstree-anchor, .jstree a, #jstree a, a[href*='doc_id']")
        if not links:
            # 备选：所有包含 doc_id 的 <a> 标签
            links = self._page.query_selector_all("a[href]")

        for link in links:
            href = link.get_attribute("href") or ""
            text = link.inner_text().strip()
            m = re.search(r"doc_id=(\d+)", href)
            if m and text:
                doc_id = m.group(1)
                if doc_id not in seen:
                    seen.add(doc_id)
                    docs.append({
                        "name": text,
                        "url": f"{BASE_URL}?doc_id={doc_id}",
                        "doc_id": doc_id,
                        "level": 1,
                    })

        # 如果 jstree 没找到链接，尝试从页面所有 <a> 提取
        if not docs:
            all_links = self._page.evaluate("""() => {
                const links = document.querySelectorAll('a[href*="doc_id"]');
                return Array.from(links).map(a => ({
                    href: a.getAttribute('href'),
                    text: a.textContent.trim()
                }));
            }""")
            for item in all_links:
                m = re.search(r"doc_id=(\d+)", item.get("href", ""))
                if m and item.get("text"):
                    doc_id = m.group(1)
                    if doc_id not in seen:
                        seen.add(doc_id)
                        docs.append({
                            "name": item["text"],
                            "url": f"{BASE_URL}?doc_id={doc_id}",
                            "doc_id": doc_id,
                            "level": 1,
                        })

        self._log(f"  发现 {len(docs)} 个文档链接")
        return docs

    # ---- 爬取单个文档 ----

    def fetch_doc(self, doc_id: str) -> Optional[str]:
        """爬取单个文档页面，返回 Markdown 内容"""
        url = f"{BASE_URL}?doc_id={doc_id}"
        try:
            self._page.goto(url, wait_until="networkidle", timeout=PAGE_LOAD_TIMEOUT)
            # 等待内容渲染
            time.sleep(2)

            # Check if we landed on login page (not logged in)
            for frame in self._page.frames:
                if "weborder" in frame.url and "login" in frame.url:
                    self._log(f"  doc_id={doc_id} 跳过: 未登录，页面跳转到登录")
                    return None

            # 尝试等待内容区域出现
            try:
                self._page.wait_for_selector(
                    "div.tui-editor-contents, div.te-preview, div.markdown-body",
                    timeout=5000,
                )
            except Exception:
                pass  # 可能选择器不匹配，继续用页面内容

            # 获取页面 HTML
            html = self._page.content()
            content = self.converter.convert(html)

            # Validate content quality - must contain API documentation markers
            if not self._is_valid_doc_content(content):
                self._log(f"  doc_id={doc_id} 跳过: 内容不是有效的API文档")
                return None

            return content

        except Exception as e:
            self._log(f"  爬取 doc_id={doc_id} 失败: {e}")
            return None

    def _is_valid_doc_content(self, content: str) -> bool:
        """Check if the content is actual API documentation, not login/navigation HTML."""
        if len(content) < 50:
            return False
        # API docs must contain at least one of these markers
        doc_markers = ["接口：", "接口:", "输入参数", "输出参数", "__输入", "__输出",
                       "接口示例", "数据样例", "限量：", "权限："]
        has_marker = any(m in content for m in doc_markers)
        # Login page markers - if present, this is NOT valid doc content
        login_markers = ["微信扫码登录", "密码登录", "验证码登录", "忘记密码"]
        is_login = any(m in content for m in login_markers)
        return has_marker and not is_login

    # ---- 内部 ----

    def _log(self, msg: str):
        if self.verbose:
            print(msg)


# =========================================================================
# 文件格式化
# =========================================================================

def format_doc_file(name: str, doc_id: str, content: str) -> str:
    title = name
    if name.startswith("API (doc_id="):
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("## ") and not line.startswith("## 基础"):
                title = line[3:].strip()
                break
    return (
        f"# {title}\n\n"
        f"**文档ID**: {doc_id}\n"
        f"**原始链接**: {BASE_URL}?doc_id={doc_id}\n\n"
        f"---\n\n"
        f"{content}\n"
    )


# =========================================================================
# README.md 索引生成
# =========================================================================

def categorize_doc(name: str) -> str:
    for cat_name, keywords in CATEGORY_KEYWORDS:
        if any(kw in name for kw in keywords):
            return cat_name
    return "其他"


def generate_readme(links: List[Dict]) -> str:
    api_docs = [d for d in links if d["doc_id"] not in CATEGORY_DOC_IDS]
    total = len(api_docs)

    categories: Dict[str, List[Dict]] = {}
    for doc in api_docs:
        cat = categorize_doc(doc["name"])
        categories.setdefault(cat, []).append(doc)

    ordered_cats = [c for c, _ in CATEGORY_KEYWORDS]
    ordered_cats.append("其他")
    ordered_cats = [c for c in ordered_cats if c in categories]

    lines = [
        "# Tushare API 接口文档索引",
        "",
        "本文档由自动化脚本从[Tushare官方文档系统](https://tushare.pro/document/2)提取。",
        "",
        "## 文档说明",
        "",
        f"- **总计**: 共提取 **{total}** 个接口文档",
        "- **格式**: 所有文档均为Markdown格式",
        "- **位置**: `skills/tushare-finance/reference/`",
        "- **更新**: 自动化提取，保持与官方文档同步",
        "- **作者**: [StanleyChanH](https://github.com/StanleyChanH)",
    ]

    for cat_name in ordered_cats:
        cat_docs = categories[cat_name]
        lines.append("")
        lines.append(f"## {cat_name}")
        lines.append("")
        lines.append(f"**数量**: {len(cat_docs)} 个接口")
        lines.append("")
        lines.append("| 序号 | 接口名称 | 文档ID | 文档路径 |")
        lines.append("|------|---------|--------|----------|")
        for i, doc in enumerate(cat_docs, 1):
            name = doc["name"]
            doc_id = doc["doc_id"]
            fname = sanitize_filename(name)
            lines.append(
                f"| {i} | {name} | {doc_id} "
                f"| [接口文档/{fname}.md](接口文档/{fname}.md) |"
            )

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 分类统计")
    lines.append("")
    lines.append("| 分类 | 接口数量 |")
    lines.append("|------|---------|")
    for cat_name in ordered_cats:
        lines.append(f"| {cat_name} | {len(categories[cat_name])} |")
    lines.append(f"| **合计** | **{total}** |")
    lines.append("")
    return "\n".join(lines)


# =========================================================================
# 主流程
# =========================================================================

def main():
    parser = argparse.ArgumentParser(description="Tushare 文档爬取与同步工具")
    parser.add_argument("--dry-run", action="store_true", help="只检测变更，不写入文件")
    parser.add_argument("--verbose", "-v", action="store_true", help="详细输出")
    parser.add_argument("--doc-id", type=str, help="只爬取指定 doc_id")
    parser.add_argument("--max-docs", type=int, default=0, help="最大爬取数（0=不限）")
    args = parser.parse_args()

    print("Tushare 文档爬取工具启动")
    print(f"   模式: {'dry-run (只检测)' if args.dry_run else '同步模式'}")
    print()

    # ---- 加载已有数据 ----
    existing_links: List[Dict] = load_json(LINKS_FILE, [])
    existing_hashes: Dict[str, str] = load_json(HASH_FILE, {})

    # ---- 启动浏览器 ----
    # Read login credentials from environment
    account = os.environ.get("TUSHARE_ACCOUNT", "")
    password = os.environ.get("TUSHARE_PASSWORD", "")
    crawler = TushareDocCrawler(
        verbose=args.verbose,
        account=account or None,
        password=password or None,
    )
    crawler.start()

    try:
        # ---- 发现文档 ----
        discovered = crawler.discover_docs()

        if not discovered:
            print("未从索引页发现文档，使用 all_links.json 作为基础")
            discovered = list(existing_links)

        # 合并已有 + 新发现
        all_docs: Dict[str, Dict] = {}
        for link in existing_links:
            all_docs[link["doc_id"]] = link
        for link in discovered:
            did = link["doc_id"]
            if did not in all_docs:
                all_docs[did] = link
                print(f"  发现新文档: {link['name']} (doc_id={did})")

        # 过滤
        if args.doc_id:
            if args.doc_id in all_docs:
                all_docs = {args.doc_id: all_docs[args.doc_id]}
            else:
                all_docs = {args.doc_id: {
                    "name": f"API (doc_id={args.doc_id})",
                    "url": f"{BASE_URL}?doc_id={args.doc_id}",
                    "doc_id": args.doc_id,
                    "level": 1,
                }}

        doc_list = sorted(all_docs.values(), key=lambda d: int(d.get("doc_id", "0")))
        if args.max_docs > 0:
            doc_list = doc_list[:args.max_docs]

        # ---- 爬取并对比 ----
        print(f"\n开始爬取 {len(doc_list)} 个文档...\n")

        stats = {"new": [], "updated": [], "unchanged": 0, "failed": []}

        for i, doc_info in enumerate(doc_list):
            doc_id = doc_info["doc_id"]
            name = doc_info.get("name", f"doc_id={doc_id}")

            print(f"  [{i + 1}/{len(doc_list)}] {name} (id={doc_id})")

            content = crawler.fetch_doc(doc_id)
            if content is None or len(content.strip()) < 30:
                print(f"    x 获取失败或内容过短")
                stats["failed"].append(doc_info)
                continue

            h = content_hash(content)
            old_h = existing_hashes.get(doc_id, "")

            if h == old_h:
                stats["unchanged"] += 1
                print(f"    - 无变更")
                continue

            formatted = format_doc_file(name, doc_id, content)
            filename = sanitize_filename(name)
            filepath = DOCS_DIR / f"{filename}.md"

            if old_h == "":
                stats["new"].append((doc_info, filename))
                print(f"    + 新文档")
            else:
                stats["updated"].append((doc_info, filename))
                print(f"    ~ 已更新")

            if not args.dry_run:
                DOCS_DIR.mkdir(parents=True, exist_ok=True)
                filepath.write_text(formatted, encoding="utf-8")
                existing_hashes[doc_id] = h

        # ---- 更新索引文件 ----
        has_changes = bool(stats["new"] or stats["updated"])

        if has_changes and not args.dry_run:
            print("\n更新索引文件...")
            updated_links = sorted(all_docs.values(), key=lambda d: int(d.get("doc_id", "0")))
            save_json(LINKS_FILE, updated_links)
            print(f"  all_links.json ({len(updated_links)} 条)")

            readme = generate_readme(updated_links)
            README_FILE.write_text(readme, encoding="utf-8")
            print(f"  README.md")

            save_json(HASH_FILE, existing_hashes)

        # ---- 输出摘要 ----
        print("\n" + "=" * 60)
        print("爬取结果摘要")
        print("=" * 60)
        print(f"  总计:     {len(doc_list)}")
        print(f"  新增:     {len(stats['new'])}")
        print(f"  更新:     {len(stats['updated'])}")
        print(f"  未变:     {stats['unchanged']}")
        print(f"  失败:     {len(stats['failed'])}")

        for label, items in [("新增", stats["new"]), ("更新", stats["updated"])]:
            if items:
                print(f"\n  {label}列表:")
                for item, fname in items:
                    print(f"    - {item.get('name', '?')} -> {fname}.md")

        if stats["failed"]:
            print(f"\n  失败列表:")
            for item in stats["failed"]:
                print(f"    - {item.get('name', '?')} (doc_id={item.get('doc_id', '?')})")

        # ---- GitHub Actions 输出 ----
        gh_output = os.environ.get("GITHUB_OUTPUT")
        if gh_output:
            with open(gh_output, "a", encoding="utf-8") as f:
                f.write(f"has_changes={'true' if has_changes else 'false'}\n")
                f.write(f"new_count={len(stats['new'])}\n")
                f.write(f"updated_count={len(stats['updated'])}\n")
                f.write(f"failed_count={len(stats['failed'])}\n")
                summary_lines = []
                for item, _ in stats["new"]:
                    summary_lines.append(f"+ {item.get('name', '?')}")
                for item, _ in stats["updated"]:
                    summary_lines.append(f"~ {item.get('name', '?')}")
                summary = "\n".join(summary_lines) if summary_lines else "no changes"
                f.write(f"change_summary<<CHANGE_SUMMARY_EOF\n{summary}\nCHANGE_SUMMARY_EOF\n")

        if args.dry_run:
            print(f"\n{'检测到变更' if has_changes else '无变更'} (dry-run)")
        else:
            print(f"\n{'同步完成' if not stats['failed'] else '同步完成（部分失败）'}")

        return 0

    finally:
        crawler.close()


if __name__ == "__main__":
    sys.exit(main())
