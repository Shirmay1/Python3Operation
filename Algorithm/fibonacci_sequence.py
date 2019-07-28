"""
日期：2019/7/28
editor:Shirmay1
题目：斐波那契数列
思路：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
    在数学上，费波那契数列是以递归的方法来定义。
"""


# 使用递归
def fib(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fib(i-1) + fib(i-2)


# 循环
def fib2(i):
    if i == 0:
        return 0
    a, b = 1, 1
    for i in range(i - 1):
        a, b = b, a + b
    return a


j = int(input('请输入要计算第几项斐波那契数列：'))
for j in range(j+1):
    print('fib({})={}'.format(j, fib(j)))
