# 本地测试指南

## 🚀 快速开始

### 1. 环境准备

#### Python 环境要求
- Python 3.7 或更高版本
- 推荐使用虚拟环境

#### 创建虚拟环境（推荐）
```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2. 安装依赖

#### 基础依赖（必需）
```bash
# 安装核心依赖
pip install arxiv pyyaml requests

# 或者安装完整依赖
pip install -r requirements.txt
```

**注意**：如果安装 `requirements.txt` 时遇到问题，可以只安装核心依赖，基础功能就能正常运行。

### 3. 配置检查

#### 验证配置文件
```bash
# 检查配置文件是否正确
python -c "import yaml; print(yaml.safe_load(open('config.yaml', 'r')))"
```

应该看到类似输出：
```python
{
    'user_name': '2502128021',
    'repo_name': 'video-generation-arxiv-daily',
    'show_badge': True,
    'keywords': {
        'Text-to-Video Generation': {...},
        'Image-to-Video Generation': {...},
        # ... 其他类别
    }
}
```

## 🧪 测试步骤

### 测试1：基础论文抓取功能

```bash
# 运行主脚本（这会生成所有文件）
python daily_arxiv.py
```

**预期结果**：
- 在 `docs/` 目录下生成多个文件
- 更新 `README.md` 文件
- 控制台输出论文抓取日志

### 测试2：单独测试特定功能

#### 测试配置加载
```python
# 创建测试脚本 test_config.py
import yaml
from daily_arxiv import load_config

config = load_config('config.yaml')
print("配置加载成功！")
print(f"用户名: {config['user_name']}")
print(f"仓库名: {config['repo_name']}")
print(f"关键词数量: {len(config['keywords'])}")
```

#### 测试论文搜索
```python
# 创建测试脚本 test_search.py
from daily_arxiv import get_daily_papers

# 测试单个类别的论文搜索
data, data_web = get_daily_papers(
    topic="Text-to-Video Generation",
    query='cat:cs.CV AND (text-to-video OR text2video OR "text to video")',
    max_results=5
)

print(f"找到 {len(data['Text-to-Video Generation'])} 篇论文")
for paper_id, content in data['Text-to-Video Generation'].items():
    print(f"论文ID: {paper_id}")
    print(f"内容: {content[:100]}...")
```

### 测试3：验证输出文件

运行后检查以下文件：

```bash
# 检查生成的文件
ls -la docs/
ls -la README.md

# 查看 README.md 内容
head -20 README.md

# 查看 JSON 数据文件
cat docs/cv-arxiv-daily.json | head -20
```

## 🐛 常见问题和解决方案

### 问题1：依赖安装失败

**错误信息**：
```
ERROR: Could not build wheels for ...
```

**解决方案**：
```bash
# 只安装核心依赖
pip install arxiv==1.4.7 pyyaml==6.0 requests==2.28.1

# 如果还有问题，尝试升级pip
pip install --upgrade pip
```

### 问题2：网络连接问题

**错误信息**：
```
requests.exceptions.ConnectionError
```

**解决方案**：
```bash
# 检查网络连接
ping arxiv.org

# 如果在中国大陆，可能需要设置代理或使用VPN
# 或者修改超时设置（在 daily_arxiv.py 中）
```

### 问题3：没有生成论文

**可能原因**：
- 关键词匹配不到最新论文
- arXiv API 限制

**解决方案**：
```bash
# 增加 max_results 参数测试
# 修改 config.yaml 中的 max_results: 20

# 或者测试更宽泛的关键词
python -c "
from daily_arxiv import get_daily_papers
data, _ = get_daily_papers('test', 'cat:cs.CV', 10)
print(f'找到 {len(data[\"test\"])} 篇论文')
"
```

### 问题4：编码问题

**错误信息**：
```
UnicodeDecodeError
```

**解决方案**：
```bash
# 确保使用 UTF-8 编码
# Windows 用户可能需要设置环境变量
set PYTHONIOENCODING=utf-8
```

## 🔧 调试技巧

### 启用详细日志
```python
# 在 daily_arxiv.py 开头修改日志级别
import logging
logging.basicConfig(
    format='[%(asctime)s %(levelname)s] %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG  # 改为 DEBUG
)
```

### 单步测试
```python
# 创建 debug.py 文件
from daily_arxiv import load_config, get_daily_papers

# 1. 测试配置加载
print("=== 测试配置加载 ===")
config = load_config('config.yaml')
print("配置加载成功")

# 2. 测试单个关键词
print("\n=== 测试论文搜索 ===")
first_keyword = list(config['keywords'].keys())[0]
query = config['kv'][first_keyword]
print(f"测试关键词: {first_keyword}")
print(f"查询语句: {query}")

data, data_web = get_daily_papers(
    topic=first_keyword,
    query=query,
    max_results=3
)

print(f"找到论文数量: {len(data[first_keyword])}")
```

## 📊 验证测试结果

### 成功标志
1. **控制台输出**：看到论文抓取日志
2. **文件生成**：`docs/` 目录下有新文件
3. **README更新**：`README.md` 包含最新论文
4. **无错误**：没有Python异常

### 输出文件检查清单
- [ ] `README.md` - 主页面更新
- [ ] `docs/index.md` - 网页版本
- [ ] `docs/wechat.md` - 微信格式
- [ ] `docs/cv-arxiv-daily.json` - JSON数据
- [ ] `docs/cv-arxiv-daily-web.json` - 网页数据

## 🎯 下一步

测试成功后，您可以：

1. **部署到GitHub**：
   - 提交代码到GitHub仓库
   - 启用GitHub Actions
   - 设置GitHub Pages

2. **配置AI分析**（可选）：
   - 参考 `API_SETUP.md`
   - 设置OpenAI API Key
   - 测试AI分析功能

3. **自定义配置**：
   - 调整关键词
   - 修改更新频率
   - 添加黑名单过滤

## 🆘 获取帮助

如果遇到问题：
1. 检查Python版本：`python --version`
2. 检查依赖安装：`pip list | grep -E "(arxiv|yaml|requests)"`
3. 查看错误日志：保存完整的错误信息
4. 尝试简化测试：只测试核心功能

测试愉快！🚀 