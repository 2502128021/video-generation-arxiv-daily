#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
配置修复脚本 - 解决文件名不匹配问题
运行命令: python fix_config.py
"""

import os
import shutil
import json

def fix_file_paths():
    """修复文件路径和文件名不匹配的问题"""
    print("🔧 开始修复配置文件问题...")
    
    # 检查docs目录是否存在
    if not os.path.exists('docs'):
        print("📁 创建docs目录...")
        os.makedirs('docs')
    
    # 文件映射关系：旧文件名 -> 新文件名
    file_mappings = {
        'docs/cv-arxiv-daily.json': 'docs/video-generation-arxiv-daily.json',
        'docs/cv-arxiv-daily-web.json': 'docs/video-generation-arxiv-daily-web.json', 
        'docs/cv-arxiv-daily-wechat.json': 'docs/video-generation-arxiv-daily-wechat.json'
    }
    
    # 重命名现有文件
    for old_path, new_path in file_mappings.items():
        if os.path.exists(old_path):
            print(f"📝 重命名文件: {old_path} -> {new_path}")
            shutil.move(old_path, new_path)
        elif not os.path.exists(new_path):
            print(f"📄 创建新文件: {new_path}")
            with open(new_path, 'w') as f:
                json.dump({}, f)
    
    # 检查并创建必要的目录和文件
    required_files = [
        'docs/video-generation-arxiv-daily.json',
        'docs/video-generation-arxiv-daily-web.json',
        'docs/video-generation-arxiv-daily-wechat.json'
    ]
    
    for file_path in required_files:
        if not os.path.exists(file_path):
            print(f"📄 创建缺失文件: {file_path}")
            with open(file_path, 'w') as f:
                json.dump({}, f)
    
    # 检查pdf_analysis目录
    if not os.path.exists('pdf_analysis'):
        print("📁 创建pdf_analysis目录...")
        os.makedirs('pdf_analysis')
    
    # 创建recent_trends.txt文件
    trends_file = 'pdf_analysis/recent_trends.txt'
    if not os.path.exists(trends_file):
        print(f"📄 创建文件: {trends_file}")
        with open(trends_file, 'w', encoding='utf-8') as f:
            f.write("视频生成领域最新趋势分析即将更新...")
    
    print("✅ 配置修复完成！")
    return True

def verify_setup():
    """验证修复结果"""
    print("\n🔍 验证修复结果...")
    
    required_files = [
        'config.yaml',
        'daily_arxiv.py',
        'docs/video-generation-arxiv-daily.json',
        'docs/video-generation-arxiv-daily-web.json',
        'docs/video-generation-arxiv-daily-wechat.json',
        'pdf_analysis/recent_trends.txt'
    ]
    
    all_good = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - 缺失")
            all_good = False
    
    if all_good:
        print("\n🎉 所有必需文件都已就位！")
        print("\n📝 下一步操作:")
        print("   1. 运行测试: python quick_test.py")
        print("   2. 运行完整脚本: python daily_arxiv.py")
        print("   3. 提交到GitHub并触发Actions")
    else:
        print("\n⚠️  仍有文件缺失，请检查上述问题")
    
    return all_good

if __name__ == "__main__":
    print("🚀 开始修复配置问题...")
    print("=" * 50)
    
    try:
        # 修复文件路径问题
        fix_file_paths()
        
        # 验证修复结果
        verify_setup()
        
        print("\n" + "=" * 50)
        print("✅ 修复完成！现在可以正常运行项目了。")
        
    except Exception as e:
        print(f"\n❌ 修复过程中出现错误: {e}")
        print("请手动检查文件结构或联系支持。") 