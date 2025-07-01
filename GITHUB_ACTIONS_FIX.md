# GitHub Actions 错误修复指南

## 🐛 问题诊断

根据您提供的错误信息，主要问题是：
```
FileNotFoundError: [Errno 2] No such file or directory: './docs/video-generation-arxiv-daily.json'
```

这个错误的根本原因是：
1. **文件名不匹配**：配置文件中指定的文件名与实际存在的文件名不一致
2. **目录结构缺失**：某些必需的文件和目录没有被正确创建
3. **文件读取逻辑**：代码没有处理文件不存在的情况

## 🔧 解决方案

### 方案1：快速修复（推荐）

**步骤1：运行修复脚本**
```bash
# 在本地运行修复脚本
python fix_config.py
```

**步骤2：验证修复结果**
```bash
# 运行快速测试
python quick_test.py

# 运行完整测试
python daily_arxiv.py
```

**步骤3：提交修复**
```bash
# 提交所有修改
git add .
git commit -m "Fix file path issues and missing directories"
git push origin main
```

### 方案2：手动修复

如果自动修复脚本无法运行，可以手动执行以下步骤：

**1. 检查并创建必需目录**
```bash
# 确保docs目录存在
mkdir -p docs
mkdir -p pdf_analysis
```

**2. 创建缺失的JSON文件**
```bash
# 创建空的JSON文件
echo '{}' > docs/video-generation-arxiv-daily.json
echo '{}' > docs/video-generation-arxiv-daily-web.json
echo '{}' > docs/video-generation-arxiv-daily-wechat.json
```

**3. 创建趋势文件**
```bash
# 创建趋势分析文件
echo "视频生成领域最新趋势分析即将更新..." > pdf_analysis/recent_trends.txt
```

**4. 重命名现有文件（如果存在）**
```bash
# 如果存在旧的文件名，重命名它们
if [ -f "docs/cv-arxiv-daily.json" ]; then
    mv docs/cv-arxiv-daily.json docs/video-generation-arxiv-daily.json
fi
if [ -f "docs/cv-arxiv-daily-web.json" ]; then
    mv docs/cv-arxiv-daily-web.json docs/video-generation-arxiv-daily-web.json
fi
if [ -f "docs/cv-arxiv-daily-wechat.json" ]; then
    mv docs/cv-arxiv-daily-wechat.json docs/video-generation-arxiv-daily-wechat.json
fi
```

## 📊 验证修复

### 必需文件检查清单
- [ ] `config.yaml` - 配置文件
- [ ] `daily_arxiv.py` - 主脚本
- [ ] `docs/video-generation-arxiv-daily.json` - README数据
- [ ] `docs/video-generation-arxiv-daily-web.json` - 网页数据
- [ ] `docs/video-generation-arxiv-daily-wechat.json` - 微信数据
- [ ] `pdf_analysis/recent_trends.txt` - 趋势分析文件

### 本地测试
```bash
# 1. 快速测试
python quick_test.py

# 2. 完整测试
python daily_arxiv.py

# 3. 检查生成的文件
ls -la docs/
ls -la README.md
```

## 🚀 GitHub Actions 重新运行

修复完成后：

1. **提交修复**：
   ```bash
   git add .
   git commit -m "Fix GitHub Actions file path issues"
   git push origin main
   ```

2. **手动触发工作流**：
   - 进入GitHub仓库
   - 点击 "Actions" 标签
   - 选择工作流
   - 点击 "Run workflow"

3. **监控执行**：
   - 查看工作流执行日志
   - 确认没有文件路径错误

## 🔍 预期结果

修复成功后，您应该看到：

**GitHub Actions 日志**：
```
[INFO] config = {...}
[INFO] Update Paper Link = False
[INFO] GET daily papers begin
[INFO] Keyword: Text-to-Video Generation
[INFO] Time = 2025-01-07 title = ... author = ...
...
[INFO] GET daily papers end
[INFO] Update Readme finished
[INFO] Update GitPage finished
[INFO] Update Wechat finished
```

**生成的文件**：
- 更新的 `README.md`
- 更新的 `docs/index.md`
- 更新的 `docs/wechat.md`
- JSON数据文件

## 🆘 如果仍有问题

### 常见问题排查

1. **权限问题**：
   ```bash
   # 确保GitHub Actions有写入权限
   # 在仓库设置 -> Actions -> General -> Workflow permissions
   # 选择 "Read and write permissions"
   ```

2. **配置文件问题**：
   ```bash
   # 检查config.yaml语法
   python -c "import yaml; print(yaml.safe_load(open('config.yaml')))"
   ```

3. **依赖问题**：
   ```bash
   # 检查requirements.txt
   pip install -r requirements.txt
   ```

### 调试技巧

1. **启用详细日志**：
   在 `daily_arxiv.py` 开头修改：
   ```python
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **本地调试**：
   ```bash
   # 逐步执行
   python -c "from daily_arxiv import load_config; print(load_config('config.yaml'))"
   ```

3. **检查GitHub Actions环境**：
   在工作流中添加调试步骤：
   ```yaml
   - name: Debug Environment
     run: |
       ls -la
       ls -la docs/
       cat config.yaml
   ```

## 💡 预防措施

为避免类似问题：

1. **定期测试**：本地运行 `python quick_test.py`
2. **版本控制**：提交前检查所有必需文件
3. **监控日志**：定期查看GitHub Actions执行日志
4. **备份数据**：保存重要的JSON数据文件

修复完成后，您的项目应该能够正常运行！🎉 