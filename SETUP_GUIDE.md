# 视频生成领域论文追踪项目部署指南

## 🚀 快速开始

### 1. Fork 和克隆项目

1. Fork 这个仓库到您的 GitHub 账户
2. 克隆到本地：
```bash
git clone https://github.com/2502128021/video-generation-arxiv-daily.git
cd video-generation-arxiv-daily
```

### 2. 修改配置文件

#### 2.1 更新 `config.yaml`
```yaml
user_name: "2502128021"  # 改为您的GitHub用户名
repo_name: "video-generation-arxiv-daily"  # 确认仓库名称
```

#### 2.2 更新 `.github/workflows/cv-arxiv-daily.yml`
```yaml
env:
  GITHUB_USER_NAME: 2502128021  # 改为您的GitHub用户名
  GITHUB_USER_EMAIL: your_email@example.com  # 改为您的邮箱
```

#### 2.3 更新 README 文件中的链接
将所有 `2502128021` 替换为您的实际 GitHub 用户名

### 3. 设置 GitHub Actions 权限

1. 进入您的仓库设置页面
2. 点击 "Actions" → "General"
3. 在 "Workflow permissions" 部分选择 "Read and write permissions"
4. 勾选 "Allow GitHub Actions to create and approve pull requests"
5. 点击 "Save"

### 4. 启用 GitHub Pages（可选）

1. 进入仓库设置页面
2. 点击 "Pages"
3. 在 "Source" 部分选择 "Deploy from a branch"
4. 选择 "main" 分支和 "/ (root)" 文件夹
5. 点击 "Save"

### 5. 测试运行

#### 5.1 手动触发 GitHub Actions
1. 进入 "Actions" 页面
2. 选择 "Run Video Generation Papers Daily" 工作流
3. 点击 "Run workflow" 按钮

#### 5.2 本地测试（可选）
```bash
# 安装依赖
pip install -r requirements.txt

# 运行脚本
python daily_arxiv.py
```

## 🔧 高级配置

### 自定义关键词

在 `config.yaml` 中修改 `keywords` 部分，添加您关注的特定领域：

```yaml
keywords:
    "Custom Category": 
        filters: ["Your", "Custom", "Keywords"]
```

### 调整更新频率

修改 `.github/workflows/cv-arxiv-daily.yml` 中的 cron 表达式：
```yaml
schedule:
  - cron: "0 0/6 * * *"  # 每6小时运行一次
  # - cron: "0 0 * * *"   # 每天运行一次
```

### 设置 AI 分析功能

#### 使用 OpenAI API
1. 获取 OpenAI API Key
2. 在仓库设置中添加 Secret：`OPENAI_API_KEY`
3. 创建 `.apikey` 文件（本地开发用）

#### 使用 Claude.ai API
1. 获取 Claude.ai Cookie
2. 创建 `.cookie` 文件
3. 运行 PDF 分析脚本

## 📊 监控和维护

### 检查运行状态
- 定期查看 "Actions" 页面确认工作流正常运行
- 检查生成的文件是否正确更新

### 处理错误
- 查看 Actions 日志排查问题
- 检查 API 限制和配额
- 更新依赖包版本

### 优化性能
- 调整 `max_results` 数量
- 优化关键词过滤规则
- 定期清理不相关的论文

## 🛠 故障排除

### 常见问题

1. **GitHub Actions 权限不足**
   - 确保已设置正确的工作流权限

2. **API 限制**
   - arXiv API 有速率限制，避免过于频繁的请求
   - PapersWithCode API 可能偶尔不可用

3. **文件路径错误**
   - 确保所有配置文件中的路径正确
   - 检查生成文件的权限

4. **关键词匹配问题**
   - 调整关键词列表
   - 检查黑名单过滤规则

### 联系支持
如果遇到问题，请：
1. 检查 GitHub Issues
2. 提交新的 Issue 描述问题
3. 包含错误日志和配置信息

## 📝 许可证

本项目采用 MIT 许可证，请查看 LICENSE 文件了解详情。 