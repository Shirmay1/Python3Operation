"""题目：暂停一秒输出，并格式化当前时间。"""
import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 2019-05-12 11:30:50
# 2019-05-12 11:30:51

# time.time()
# Out[22]: 1557037853.3273404
# time.localtime()
# Out[23]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=5, tm_hour=14, tm_min=31, tm_sec=43, tm_wday=6, tm_yday=125, tm_isdst=0)
# time.gmtime()
# Out[24]: time.struct_time(tm_year=2019, tm_mon=5, tm_mday=5, tm_hour=6, tm_min=32, tm_sec=2, tm_wday=6, tm_yday=125, tm_isdst=0)
# time.asctime()
# Out[25]: 'Sun May  5 14:32:22 2019'
# time.ctime()
# Out[26]: 'Sun May  5 14:32:32 2019'
# time.strftime('%y-%m-%d', time.localtime())
# Out[27]: '19-05-05'
