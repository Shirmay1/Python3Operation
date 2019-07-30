"""
题目：斐波那契数列。
程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
在数学上，费波那契数列是以递归的方法来定义：
"""

# 使用递归
def fun1(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fun1(n-1) + fun1(n-2)


# 循环
def fun2(n):
    if n == 0:
        return 0
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


print(fun1(10))
print(fun2(10))
