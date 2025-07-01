# API 配置指南

## 🤖 AI 论文分析功能设置

### 重要说明
- **基础功能**：论文抓取和更新功能无需任何API Key
- **AI分析功能**：仅在需要论文内容分析时才需要配置API

## 🔧 OpenAI API 配置（推荐）

### 1. 获取 OpenAI API Key
1. 访问 [OpenAI Platform](https://platform.openai.com/)
2. 注册/登录账户
3. 进入 "API Keys" 页面
4. 点击 "Create new secret key"
5. 复制生成的API Key

### 2. 设置API Key

#### 方法一：GitHub Secrets（用于GitHub Actions）
1. 进入您的仓库设置页面
2. 点击 "Secrets and variables" → "Actions"
3. 点击 "New repository secret"
4. Name: `OPENAI_API_KEY`
5. Secret: 粘贴您的API Key
6. 点击 "Add secret"

#### 方法二：本地开发（用于本地测试）
在项目根目录创建 `.apikey` 文件：
```bash
echo "your-openai-api-key-here" > .apikey
```

### 3. 修改 GitHub Actions 工作流

如果要在自动化流程中启用AI分析，需要修改 `.github/workflows/cv-arxiv-daily.yml`：

```yaml
# 在 steps 中添加以下步骤（在 "Run daily arxiv" 之后）
- name: Run AI Analysis (Optional)
  env:
    OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
  run: |
    if [ ! -z "$OPENAI_API_KEY" ]; then
      echo "$OPENAI_API_KEY" > .apikey
      cd pdf_analysis
      python download_pdf.py
      python parse_pdf.py
      python analysis_papers.py --api openai
      python generating_paper_analysis.py
    else
      echo "OPENAI_API_KEY not set, skipping AI analysis"
    fi
```

### 4. 本地运行AI分析

```bash
# 1. 下载PDF文件
cd pdf_analysis
python download_pdf.py

# 2. 解析PDF为文本
python parse_pdf.py

# 3. 运行AI分析
python analysis_papers.py --api openai

# 4. 生成分析报告
python generating_paper_analysis.py
```

## 🔮 Claude.ai API 配置（备选）

### 1. 获取 Claude.ai Cookie
1. 登录 [Claude.ai](https://claude.ai/)
2. 打开浏览器开发者工具 (F12)
3. 进入 "Application" → "Cookies"
4. 复制 Cookie 值

### 2. 设置 Cookie
在项目根目录创建 `.cookie` 文件：
```bash
echo "your-claude-cookie-here" > .cookie
```

### 3. 运行 Claude 分析
```bash
cd pdf_analysis
python analysis_papers.py --api claudeai --apikey .cookie
```

## 💰 成本估算

### OpenAI API 成本（GPT-4o）
- 输入：$2.50 / 1M tokens
- 输出：$10.00 / 1M tokens
- 单篇论文分析约 0.01-0.05 美元
- 每月分析100篇论文约 1-5 美元

### Claude.ai
- 免费版：有使用限制
- Pro版：$20/月 无限使用

## 🔄 启用/禁用AI分析

### 完全禁用AI分析
如果不需要AI分析功能，保持当前配置即可，项目会正常运行基础的论文抓取功能。

### 按需启用AI分析
可以手动触发AI分析，而不在自动化流程中包含：
```bash
# 仅在需要时手动运行
cd pdf_analysis
python analysis_papers.py
```

## ⚠️ 注意事项

1. **API Key 安全**：
   - 永远不要将API Key提交到代码仓库
   - 使用 `.gitignore` 忽略 `.apikey` 和 `.cookie` 文件

2. **成本控制**：
   - 设置OpenAI账户的使用限额
   - 监控API使用情况

3. **速率限制**：
   - OpenAI API有速率限制
   - 建议在分析脚本中添加适当的延迟

4. **可选功能**：
   - AI分析是可选功能，不影响核心论文抓取
   - 可以先运行基础功能，后续再添加AI分析 