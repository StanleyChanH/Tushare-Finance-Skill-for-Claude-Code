# Tushare Finance Skill

[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code)
[![License](https://img.shields.io/badge/license-Apache--2.0-green.svg)](LICENSE)
[![ClawHub](https://img.shields.io/badge/ClawHub-Available-purple.svg)](https://clawhub.com)
[![Auto Sync](https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/actions/workflows/sync-docs.yml/badge.svg)](https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/actions/workflows/sync-docs.yml)

获取中国金融市场数据的 OpenClaw Skill，支持 **220+ 个 Tushare Pro 接口**。

## ✨ 特性

- 🚀 **开箱即用** - 一键安装，无需复杂配置
- 📊 **全面覆盖** - A股、港股、美股、基金、期货、债券
- 🔧 **多种方式** - Python API、命令行工具、批量导出
- 📈 **实时数据** - 支持股票行情、财务报表、宏观经济
- 🔄 **OpenClaw 集成** - 无缝集成到自动化工作流
- 📖 **完整文档** - 220+ 接口完整索引和使用示例
- 🤖 **自动同步** - GitHub Actions 定期爬取官方文档，自动更新

## 📥 安装

### 方法 1：通过 ClawHub（推荐）

```bash
clawhub install tushare-finance
```

### 方法 2：手动安装

```bash
git clone https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code.git
cd Tushare-Finance-Skill-for-Claude-Code
pip install -r requirements.txt
```

## 🔑 配置

### 获取 Tushare Token

1. 访问 [Tushare Pro](https://tushare.pro) 注册账号
2. 在个人中心获取 Token
3. 配置环境变量：

```bash
export TUSHARE_TOKEN="your_token_here"
```

## 🚀 快速开始

### Python API

```python
from scripts.api_client import TushareAPI

# 初始化客户端
api = TushareAPI()

# 查询股票日线行情
df = api.get_stock_daily("000001.SZ", "2024-01-01", "2024-12-31")
print(df.head())

# 查询公司基本信息
info = api.get_stock_info("000001.SZ")
print(info)

# 批量查询多只股票
stocks = ["000001.SZ", "000002.SZ", "600000.SH"]
data = api.batch_query(stocks, "2024-01-01", "2024-12-31")
```

## 📊 支持的数据类型

| 类别 | 接口数量 | 示例接口 |
|------|---------|---------|
| 股票数据 | 39 | `daily`, `stock_basic`, `fina_indicator`, `income` |
| 指数专题 | 18 | `index_daily`, `index_weight`, `index_basic` |
| 公募基金 | 11 | `fund_nav`, `fund_basic`, `fund_hold` |
| 期货期权 | 16 | `futures_daily`, `opt_daily` |
| 宏观经济 | 10 | `gdp`, `cpi`, `pmi`, `shibor` |
| 港股美股 | 23 | `hk_daily`, `us_daily` |
| 债券专题 | 16 | `cb_basic`, `cb_price` |
| ETF专题 | 7 | `etf_basic`, `fund_etf_hist` |
| 大模型语料 | 7 | `news`, `anns`, `policy` |
| 行业经济 | 8 | `movie`, `box_office` |

**完整接口列表**：查看 [接口文档索引](reference/README.md)

## 🤖 文档自动同步

本项目通过 GitHub Actions 自动从 [Tushare 官方文档](https://tushare.pro/document/2) 同步 API 文档。

### 工作流程

```
每周一 10:00 CST (自动) / 手动触发
    │
    ├─ Playwright 登录 Tushare
    ├─ ddddocr 自动识别验证码
    ├─ 爬取 220+ 文档页面
    ├─ SHA256 增量对比，只更新有变更的文档
    ├─ 内容质量校验
    └─ 自动创建 Pull Request
```

### 手动触发

在 GitHub Actions 页面点击 **"Run workflow"**，支持以下参数：

| 参数 | 说明 |
|------|------|
| `dry_run` | 只检测变更，不写入文件 |
| `max_docs` | 最大爬取数量（测试用） |
| `doc_id` | 只爬取指定文档 |

### 配置 Secrets

需要在仓库 Settings → Secrets 中配置：

| Secret | 说明 |
|--------|------|
| `TUSHARE_ACCOUNT` | Tushare 登录手机号或邮箱 |
| `TUSHARE_PASSWORD` | Tushare 登录密码 |

## 📖 文档结构

```
├── SKILL.md              # Skill 定义文件
├── QUICK_REFERENCE.md    # 快速参考
├── scripts/
│   ├── api_client.py     # Python API 客户端
│   └── crawl_docs.py     # 文档自动同步爬虫
├── reference/
│   ├── README.md         # 接口文档索引
│   ├── all_links.json    # 全部接口链接
│   └── 接口文档/          # 220+ 个接口 Markdown 文件
└── .github/workflows/
    ├── sync-docs.yml     # 文档自动同步工作流
    └── sync-to-clawhub.yml # ClawHub 发布工作流
```

## 🤝 贡献

欢迎贡献代码、报告问题或提出建议！

## 📄 许可证

Apache License 2.0

## 🙏 致谢

- [Tushare Pro](https://tushare.pro) - 提供高质量金融数据 API
- [OpenClaw](https://github.com/openclaw/openclaw) - OpenClaw 框架

## 📚 相关资源

- **GitHub**：https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code
- **ClawHub**：https://clawhub.com/skill/tushare-finance
- **Tushare 文档**：https://tushare.pro/document/2

## 📊 更新日志

### v2.1.0 (2026-06-09)
- 🤖 新增 GitHub Actions 文档自动同步（每周一 + 手动触发）
- 🔐 支持 Playwright + ddddocr 自动登录并识别验证码
- 📊 SHA256 增量对比，只更新有变更的文档
- ✅ 内容质量校验，自动过滤非文档内容
- 🔄 自动创建 PR，包含变更统计
- 📖 自动更新 `all_links.json` 和 `README.md` 索引

### v2.0.6 (2026-06-08)
- 🐛 修复 ClawHub CLI 超时问题

### v2.0.0 (2026-02-14)
- ✨ 添加完整的 Python API 客户端
- ✨ 添加命令行工具
- ✨ 添加批量导出功能
- 📖 完善 API 文档和使用示例
- 🔄 配置 GitHub Actions 自动发布

### v1.0.0 (2026-01-10)
- 🎉 初始版本发布
- 📊 支持 220+ Tushare Pro 接口
