#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
快速测试脚本 - 验证项目核心功能
运行命令: python quick_test.py
"""

import os
import sys
import traceback

def test_imports():
    """测试依赖导入"""
    print("🔍 测试依赖导入...")
    try:
        import arxiv
        import yaml  
        import requests
        print("✅ 核心依赖导入成功")
        return True
    except ImportError as e:
        print(f"❌ 依赖导入失败: {e}")
        print("请运行: pip install arxiv pyyaml requests")
        return False

def test_config():
    """测试配置文件"""
    print("\n🔍 测试配置文件...")
    try:
        from daily_arxiv import load_config
        config = load_config('config.yaml')
        print(f"✅ 配置加载成功")
        print(f"   用户名: {config['user_name']}")
        print(f"   仓库名: {config['repo_name']}")
        print(f"   关键词类别数: {len(config['keywords'])}")
        return config
    except Exception as e:
        print(f"❌ 配置加载失败: {e}")
        return None

def test_arxiv_connection():
    """测试arXiv连接"""
    print("\n🔍 测试arXiv API连接...")
    try:
        import arxiv
        # 简单的测试查询
        search = arxiv.Search(
            query="cat:cs.CV",
            max_results=1,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        
        results = list(search.results())
        if results:
            paper = results[0]
            print(f"✅ arXiv连接成功")
            print(f"   测试论文: {paper.title[:50]}...")
            return True
        else:
            print("⚠️  arXiv连接成功但未获取到论文")
            return False
    except Exception as e:
        print(f"❌ arXiv连接失败: {e}")
        return False

def test_paper_search():
    """测试论文搜索功能"""
    print("\n🔍 测试论文搜索功能...")
    try:
        from daily_arxiv import get_daily_papers
        
        # 测试一个简单的查询
        data, data_web = get_daily_papers(
            topic="Test Category",
            query='cat:cs.CV AND (video OR generation)',
            max_results=3
        )
        
        paper_count = len(data.get("Test Category", {}))
        print(f"✅ 论文搜索成功，找到 {paper_count} 篇论文")
        
        if paper_count > 0:
            # 显示第一篇论文的信息
            first_paper = list(data["Test Category"].items())[0]
            print(f"   示例论文ID: {first_paper[0]}")
            print(f"   论文信息: {first_paper[1][:80]}...")
        
        return paper_count > 0
    except Exception as e:
        print(f"❌ 论文搜索失败: {e}")
        traceback.print_exc()
        return False

def test_full_pipeline():
    """测试完整流程"""
    print("\n🔍 测试完整流程...")
    try:
        # 运行主脚本的核心功能
        from daily_arxiv import load_config, get_daily_papers
        
        config = load_config('config.yaml')
        
        # 只测试第一个关键词类别
        first_category = list(config['keywords'].keys())[0]
        query = config['kv'][first_category]
        
        print(f"   测试类别: {first_category}")
        print(f"   查询语句: {query[:50]}...")
        
        data, data_web = get_daily_papers(
            topic=first_category,
            query=query,
            max_results=5
        )
        
        paper_count = len(data.get(first_category, {}))
        print(f"✅ 完整流程测试成功，{first_category} 类别找到 {paper_count} 篇论文")
        return True
        
    except Exception as e:
        print(f"❌ 完整流程测试失败: {e}")
        traceback.print_exc()
        return False

def main():
    """主测试函数"""
    print("🚀 开始快速测试...")
    print("=" * 50)
    
    # 检查当前目录
    if not os.path.exists('config.yaml'):
        print("❌ 未找到 config.yaml 文件，请确保在项目根目录运行此脚本")
        return False
    
    if not os.path.exists('daily_arxiv.py'):
        print("❌ 未找到 daily_arxiv.py 文件，请确保在项目根目录运行此脚本")
        return False
    
    # 运行测试
    tests = [
        ("依赖导入", test_imports),
        ("配置文件", test_config), 
        ("arXiv连接", test_arxiv_connection),
        ("论文搜索", test_paper_search),
        ("完整流程", test_full_pipeline)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
            if not result and test_name in ["依赖导入", "配置文件"]:
                print(f"\n❌ {test_name} 测试失败，停止后续测试")
                break
        except Exception as e:
            print(f"\n❌ {test_name} 测试出现异常: {e}")
            results.append((test_name, False))
    
    # 输出测试结果总结
    print("\n" + "=" * 50)
    print("📊 测试结果总结:")
    
    passed = 0
    for test_name, result in results:
        status = "✅ 通过" if result else "❌ 失败"
        print(f"   {test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\n总计: {passed}/{len(results)} 项测试通过")
    
    if passed == len(results):
        print("\n🎉 所有测试通过！您的项目配置正确，可以正常运行。")
        print("\n📝 下一步操作:")
        print("   1. 运行完整脚本: python daily_arxiv.py")
        print("   2. 检查生成的文件: docs/ 目录和 README.md")
        print("   3. 部署到GitHub并启用GitHub Actions")
    elif passed >= 3:
        print("\n⚠️  大部分测试通过，基础功能应该可以正常运行。")
        print("   建议直接运行: python daily_arxiv.py")
    else:
        print("\n❌ 多项测试失败，请检查环境配置。")
        print("\n🔧 建议操作:")
        print("   1. 检查Python版本: python --version")
        print("   2. 安装依赖: pip install arxiv pyyaml requests")
        print("   3. 检查网络连接")
        print("   4. 查看详细错误信息")
    
    return passed == len(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 