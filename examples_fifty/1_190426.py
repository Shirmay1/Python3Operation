"""
日期：2019/4/26
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
"""
for i in range(1, 5):
    for j in range(1, 5):
        for h in range(1, 5):
            if i != j and j != h and i != h:
                result = i*100 + j*10 + h
                print(result)
