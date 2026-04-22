#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime

def generate_daily_report(date=None):
    """
    根据日期生成每日行情记录文件
    
    Args:
        date: 日期对象或字符串，默认为今天
    """
    if date is None:
        date = datetime.now()
    elif isinstance(date, str):
        date = datetime.strptime(date, "%Y-%m-%d")
    
    # 文件名
    filename = f"{date.strftime('%Y-%m-%d')}.md"
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
    
    # 模板内容
    template = f"""### 4月{date.strftime('%d')}日 强势板块个股

| 股票代码 | 股票名称 | 概念/板块 | 涨跌幅 | 备注 |
| :--- | :--- | :--- | :--- | :--- |

### 4月{date.strftime('%d')}日 调整板块个股

| 股票代码 | 股票名称 | 概念/板块 | 涨跌幅 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
"""
    
    # 写入文件
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(template)
    
    print(f"已生成文件: {filename}")
    print(f"日期: {date.strftime('%Y-%m-%d')}")
    print(f"路径: {filepath}")
    
    return filepath

if __name__ == "__main__":
    import sys
    
    # 支持命令行参数
    if len(sys.argv) > 1:
        date_str = sys.argv[1]
        generate_daily_report(date_str)
    else:
        # 默认使用今天
        generate_daily_report()
