"""
题目：输出指定格式的日期。
程序分析：使用 time, datetime 模块。
"""

import time
import datetime
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))
print(time.strftime("%Y-%m-%d %X"))
print(datetime.date(1941, 1, 5).strftime('%Y/%m/%d'))
