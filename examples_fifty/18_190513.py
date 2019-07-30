"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""
n = int(input('请输入个数n：'))
a = int(input('请输入数字a:'))
s = 0
Sn = 0
for i in range(n):
    t = a * 10**i
    s += t
    Sn += s
print('计算和为：', Sn)
