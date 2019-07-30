"""
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
"""

numlist = []
for i in range(3):
    num = input('请输入一个整数：')
    numlist.append(num)
numlist.sort()
for i in numlist:
    print('从小到大输出为：', i)
