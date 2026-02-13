# GitHub Actions 自动同步配置

本项目使用 GitHub Actions 实现自动同步到 ClawHub。

## 配置步骤

### 1. 获取 ClawHub Token

```bash
# 登录 ClawHub（本地执行）
clawhub login

# 查看你的 token
clawhub whoami
# Token 通常存储在 ~/.config/clawhub/config.json
```

### 2. 配置 GitHub Secrets

1. 进入 GitHub 仓库设置页面
2. 导航到 **Settings** → **Secrets and variables** → **Actions**
3. 点击 **New repository secret**
4. 添加以下 secret：
   - **Name**: `CLAWHUB_TOKEN`
   - **Value**: 你的 ClawHub token（从 `~/.config/clawhub/config.json` 复制）

### 3. 测试自动同步

```bash
# 修改 metadata.json 中的版本号
# 例如：2.0.0 → 2.0.1

# 提交并推送
git add metadata.json
git commit -m "Bump version to 2.0.1"
git push origin master

# GitHub Actions 会自动触发：
# 1. 发布到 ClawHub
# 2. 创建 GitHub Release
```

## 工作流程说明

当你推送代码到 `master` 分支时，如果修改了以下文件，会自动触发同步：

- `SKILL.md`
- `metadata.json`
- `README.md`
- `scripts/**`
- `reference/**`

### 自动化步骤

1. ✅ 检出代码
2. ✅ 安装 ClawHub CLI
3. ✅ 使用 `CLAWHUB_TOKEN` 认证
4. ✅ 从 `metadata.json` 读取版本号
5. ✅ 发布到 ClawHub
6. ✅ 创建 GitHub Release

## 注意事项

- **首次配置**：需要手动在 GitHub 仓库中添加 `CLAWHUB_TOKEN` secret
- **版本号**：每次更新前记得修改 `metadata.json` 中的版本号
- **速率限制**：ClawHub 有发布速率限制，避免频繁推送
- **失败重试**：如果发布失败，可以在 GitHub Actions 页面手动重新运行

## 手动发布（备用方案）

如果自动同步失败，可以手动发布：

```bash
# 本地执行
clawhub publish . --slug tushare-finance --name "tushare-finance" --version 2.0.1 --changelog "手动发布"
```

## 查看同步状态

- **GitHub Actions**: https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/actions
- **ClawHub 页面**: https://clawhub.com/skill/tushare-finance
- **GitHub Releases**: https://github.com/StanleyChanH/Tushare-Finance-Skill-for-Claude-Code/releases
