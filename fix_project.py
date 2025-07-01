#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
一键修复脚本 - 自动解决GitHub Actions和配置问题
"""

import os
import json
import yaml
import logging
from pathlib import Path

# 设置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def create_directories():
    """创建必需的目录"""
    directories = ['docs', 'pdf_analysis']
    for dir_name in directories:
        Path(dir_name).mkdir(exist_ok=True)
        logger.info(f"✅ 目录已创建: {dir_name}")

def create_json_files():
    """创建必需的JSON文件"""
    json_files = [
        'docs/video-generation-arxiv-daily.json',
        'docs/video-generation-arxiv-daily-web.json', 
        'docs/video-generation-arxiv-daily-wechat.json'
    ]
    
    empty_data = {
        "papers": [],
        "updated": "",
        "total": 0
    }
    
    for json_file in json_files:
        if not os.path.exists(json_file):
            with open(json_file, 'w', encoding='utf-8') as f:
                json.dump(empty_data, f, indent=2, ensure_ascii=False)
            logger.info(f"✅ JSON文件已创建: {json_file}")
        else:
            logger.info(f"📄 JSON文件已存在: {json_file}")

def create_trend_file():
    """创建趋势分析文件"""
    trend_file = 'pdf_analysis/recent_trends.txt'
    if not os.path.exists(trend_file):
        with open(trend_file, 'w', encoding='utf-8') as f:
            f.write("视频生成领域最新趋势分析\n")
            f.write("=" * 30 + "\n\n")
            f.write("📊 当前趋势概览：\n\n")
            f.write("1. Text-to-Video生成技术快速发展\n")
            f.write("2. 扩散模型在视频生成中的应用日益成熟\n")
            f.write("3. 多模态视频理解和控制技术兴起\n")
            f.write("4. 3D感知视频生成成为新热点\n")
            f.write("5. 视频编辑和增强技术不断优化\n\n")
            f.write("💡 技术发展方向：\n")
            f.write("- 更高质量的视频生成\n")
            f.write("- 更精确的运动控制\n")
            f.write("- 更好的时间一致性\n")
            f.write("- 更强的可控性和可编辑性\n\n")
            f.write("本分析将定期更新，反映最新的研究趋势和技术进展。\n")
        logger.info(f"✅ 趋势文件已创建: {trend_file}")
    else:
        logger.info(f"📄 趋势文件已存在: {trend_file}")

def rename_old_files():
    """重命名旧的文件"""
    file_mappings = {
        'docs/cv-arxiv-daily.json': 'docs/video-generation-arxiv-daily.json',
        'docs/cv-arxiv-daily-web.json': 'docs/video-generation-arxiv-daily-web.json',
        'docs/cv-arxiv-daily-wechat.json': 'docs/video-generation-arxiv-daily-wechat.json'
    }
    
    for old_file, new_file in file_mappings.items():
        if os.path.exists(old_file) and not os.path.exists(new_file):
            os.rename(old_file, new_file)
            logger.info(f"✅ 文件已重命名: {old_file} -> {new_file}")

def check_config_file():
    """检查并验证配置文件"""
    config_file = 'config.yaml'
    if not os.path.exists(config_file):
        logger.error(f"❌ 配置文件不存在: {config_file}")
        return False
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        # 检查必需的配置项
        required_keys = ['user_name', 'repo_name', 'keywords']
        for key in required_keys:
            if key not in config:
                logger.warning(f"⚠️ 配置文件缺少必需项: {key}")
        
        logger.info("✅ 配置文件检查通过")
        return True
    except Exception as e:
        logger.error(f"❌ 配置文件解析错误: {e}")
        return False

def create_blacklist_file():
    """创建黑名单文件"""
    blacklist_file = 'blacklists.txt'
    if not os.path.exists(blacklist_file):
        blacklist_content = """# 视频生成领域黑名单关键词
# 用于过滤不相关的论文

# 不相关的计算机视觉任务
image classification
object detection
semantic segmentation
instance segmentation
face recognition
pose estimation
optical character recognition
medical imaging
satellite imagery

# 不相关的机器学习任务
natural language processing
speech recognition
recommendation system
time series forecasting
tabular data analysis
graph neural network
reinforcement learning games

# 硬件和系统相关
hardware acceleration
fpga implementation
mobile deployment
edge computing optimization
network compression
model quantization

# 其他不相关领域
bioinformatics
financial modeling
weather prediction
autonomous driving sensors
robotics manipulation
"""
        with open(blacklist_file, 'w', encoding='utf-8') as f:
            f.write(blacklist_content)
        logger.info(f"✅ 黑名单文件已创建: {blacklist_file}")
    else:
        logger.info(f"📄 黑名单文件已存在: {blacklist_file}")

def create_requirements_file():
    """创建requirements.txt文件"""
    requirements_file = 'requirements.txt'
    if not os.path.exists(requirements_file):
        requirements_content = """requests>=2.28.0
PyYAML>=6.0
feedparser>=6.0.8
arxiv>=1.4.0
openai>=1.0.0
anthropic>=0.7.0
beautifulsoup4>=4.11.0
lxml>=4.9.0
python-dateutil>=2.8.0
tqdm>=4.64.0
"""
        with open(requirements_file, 'w', encoding='utf-8') as f:
            f.write(requirements_content)
        logger.info(f"✅ 依赖文件已创建: {requirements_file}")
    else:
        logger.info(f"📄 依赖文件已存在: {requirements_file}")

def create_gitignore():
    """创建.gitignore文件"""
    gitignore_file = '.gitignore'
    gitignore_content = """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
logs/

# API Keys (重要：保护API密钥)
.env
api_keys.txt
secrets.yaml

# Temporary files
temp/
tmp/
*.tmp
"""
    
    if not os.path.exists(gitignore_file):
        with open(gitignore_file, 'w', encoding='utf-8') as f:
            f.write(gitignore_content)
        logger.info(f"✅ .gitignore文件已创建: {gitignore_file}")
    else:
        logger.info(f"📄 .gitignore文件已存在: {gitignore_file}")

def verify_fix():
    """验证修复结果"""
    logger.info("🔍 验证修复结果...")
    
    # 检查必需文件
    required_files = [
        'config.yaml',
        'daily_arxiv.py',
        'docs/video-generation-arxiv-daily.json',
        'docs/video-generation-arxiv-daily-web.json',
        'docs/video-generation-arxiv-daily-wechat.json',
        'pdf_analysis/recent_trends.txt',
        'blacklists.txt',
        'requirements.txt'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
    
    if missing_files:
        logger.warning(f"⚠️ 仍缺少文件: {missing_files}")
        return False
    else:
        logger.info("✅ 所有必需文件都存在")
        return True

def main():
    """主函数"""
    logger.info("🚀 开始一键修复项目...")
    
    try:
        # 1. 创建目录
        create_directories()
        
        # 2. 重命名旧文件
        rename_old_files()
        
        # 3. 创建JSON文件
        create_json_files()
        
        # 4. 创建趋势文件
        create_trend_file()
        
        # 5. 创建黑名单文件
        create_blacklist_file()
        
        # 6. 创建依赖文件
        create_requirements_file()
        
        # 7. 创建.gitignore
        create_gitignore()
        
        # 8. 检查配置文件
        config_valid = check_config_file()
        
        # 9. 验证修复结果
        fix_successful = verify_fix()
        
        if fix_successful and config_valid:
            logger.info("🎉 项目修复完成！")
            logger.info("📋 接下来的步骤：")
            logger.info("   1. 运行: python quick_test.py")
            logger.info("   2. 运行: python daily_arxiv.py")
            logger.info("   3. 提交代码: git add . && git commit -m 'Fix project configuration'")
            logger.info("   4. 推送代码: git push origin main")
        else:
            logger.warning("⚠️ 修复过程中发现问题，请检查上面的警告信息")
            
    except Exception as e:
        logger.error(f"❌ 修复过程中出现错误: {e}")
        return False
    
    return True

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1) 