# Tushare Finance Skill for Claude Code

一个专为 Claude Code 设计的 [Tushare Pro](https://tushare.pro) 金融数据获取 Skill，支持 220+ 个金融数据接口。

**作者**: [StanleyChanH](https://github.com/StanleyChanH)

## 特性

- 🎯 **全面的数据覆盖** - 支持 220+ 个 Tushare API 接口
- 💬 **自然语言交互** - 直接用中文描述需求即可获取数据
- 📊 **丰富的数据类型** - 股票、财务、指数、宏观经济等
- 🚀 **开箱即用** - Claude Code Skill 即插即用
- 📚 **完整的接口文档** - 包含 220+ 个接口的详细文档
- ✨ **符合官方标准** - 遵循 Claude Code Skills 最佳实践

## 安装

### 1. 安装依赖

```bash
pip install tushare pandas
```

### 2. 配置 Token

访问 [Tushare 官网](https://tushare.pro) 注册账号并获取 API token：

```bash
export TUSHARE_TOKEN="your_token_here"
```

### 3. 安装 Skill

将 skill 文件复制到 Claude Code 的 skills 目录：

```bash
cp -r skills/tushare-finance ~/.claude/skills/
```

## 使用方法

安装后，在 Claude Code 中直接对话：

**获取股票数据**：
```
获取平安银行最近 30 天的股价数据
```

**财务分析**：
```
查看招商银行最近的财务报表，分析营收和净利润
```

**股票筛选**：
```
帮我查找所有银行股并分析最近表现
```

**指数数据**：
```
获取上证指数最近的行情数据
```

**宏观数据**：
```
查询最近一年的 GDP 和 CPI 数据
```

## 工作原理

### Skill 如何工作

1. **自动触发**：当用户询问金融数据相关问题时自动触发
2. **查阅接口**：Claude 查看 `reference/README.md` 了解可用接口
3. **读取文档**：查看具体接口文档了解参数和用法
4. **编写代码**：直接调用 `tushare` 库生成代码
5. **获取数据**：执行代码并展示结果

### 渐进式披露

本 skill 采用 Claude Code 官方推荐的渐进式披露策略：

- **SKILL.md**（90 行）：核心指引和快速开始
- **QUICK_REFERENCE.md**：常用代码示例和最佳实践
- **reference/**（220+ 个接口）：详细文档，按需加载

Claude 会根据任务需要自动读取相应文档，无需一次性加载所有内容。

### 项目结构

```
TushareAPI_Skill/
├── README.md                  ⭐ 项目说明
├── LICENSE                    MIT 许可证
├── .gitignore                 Git 忽略
├── requirements.txt           Python 依赖
│
└── skills/                    Claude Code Skills
    └── tushare-finance/       主 Skill（完整、自包含）
        ├── SKILL.md          ⭐ Skill 定义（核心指引）
        ├── QUICK_REFERENCE.md  快速参考（代码示例）
        └── reference/        接口文档（220+ 个）
            ├── README.md     接口索引
            ├── all_links.json
            └── 接口文档/     详细文档
```

## 支持的数据接口

| 分类 | 接口数量 | 主要接口 |
|------|---------|---------|
| 股票数据 | 39 | stock_basic, daily, income, balancesheet |
| 指数数据 | 18 | index_basic, index_daily, index_weight |
| 基金数据 | 11 | fund_basic, fund_daily, fund_nav |
| 期货期权 | 16 | fut_basic, fut_daily, opt_basic |
| 宏观经济 | 10 | gdp, cpi, pmi, shibor, lpr |
| 港股美股 | 23 | hk_basic, hk_daily, us_basic |
| 债券数据 | 16 | bond_basic, bond_cb |

**完整列表**：查看 [接口文档索引](skills/tushare-finance/reference/README.md)

## Skill 特性

本 skill 遵循 [Claude Code Skills 官方文档](https://code.claude.com/docs/zh-CN/skills) 标准：

### YAML Frontmatter
- ✅ **name**: `tushare-finance` - 唯一标识符
- ✅ **description**: 明确功能和触发场景
- ✅ **allowed-tools**: 限制工具权限（Bash Python 执行，Read 文档读取）

### 自动触发
Skill 会在以下情况自动激活：
- 用户请求股价、财务数据
- 查询指数、基金、期货、债券
- 获取宏观经济指标（GDP、CPI、利率等）
- 金融数据分析和可视化

### 工具权限
- `Bash(python:*)`: 允许执行 Python 代码
- `Read`: 允许读取接口文档

## API 限制说明

### 基础积分（免费）
- 每分钟 500 次请求
- 每次最多 6000 条数据
- 基础行情、财务数据等接口

### 高级接口
- 部分接口需要 2000 积分起
- VIP 接口需要 5000 积分
- 详见 [Tushare 官方文档](https://tushare.pro/document/1)

## 参考资源

- [Tushare 官方文档](https://tushare.pro/document/2)
- [Claude Code 文档](https://code.claude.com/docs/zh-CN/skills)
- [Anthropic Skills 仓库](https://github.com/anthropics/skills)

## 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

---

**注意**: 本项目仅供学习和研究使用，请勿用于商业用途。使用时请遵守 Tushare 的使用条款。
