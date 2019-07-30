"""
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多
程序分析：兔子的规律为数列1,1,2,3,5,8,13,21....
"""


# 方法一：
def fun(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fun(n-1) + fun(n-2)
num = {}
for i in range(1, 22):
    rabitnum = fun(i)
    num[str(i)] = rabitnum
print(num)


# 方法二
f1 = 1
f2 = 1
for i in range(1, 22):
    print('{:10d} {:10d}'.format(f1, f2), end='')
    if (i % 3) == 0:
        print('')
    f1 = f1 + f2
    f2 = f1 + f2


# 方法三
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a
num = {}
for i in range(1, 22):
    rabitnum = fib(i)
    num[str(i)] = rabitnum
print(num)
