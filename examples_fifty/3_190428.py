"""
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

"""
# 方法一：由于题目中加上100是一个完全平方数，所以，这个数最小为-99.

for t in range(-99, 10000):
    j = (t+100)**0.5
    m = (t+100+168)**0.5
    if int(j)*int(j) == t+100 and int(m)*int(m) == t+100+168:
        print(t)
        

# 方法二: https://www.runoob.com/python/python-exercise-example3.html
# 问题:输出结果为浮点数
"""
1、则：x + 100 = n2, x + 100 + 168 = m2
2、计算等式：m2 - n2 = (m + n)(m - n) = 168
3、设置： m + n = i，m - n = j，i * j =168，i 和 j 至少一个是偶数
4、可得： m = (i + j) / 2， n = (i - j) / 2，i 和 j 要么都是偶数，要么都是奇数。
5、从 3 和 4 推导可知道，i 与 j 均是大于等于 2 的偶数。
6、由于 i * j = 168， j>=2，则 1 < i < 168 / 2 + 1。
7、接下来将 i 的所有数字循环计算即可。
"""
for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            x = n * n - 100
            print(x)