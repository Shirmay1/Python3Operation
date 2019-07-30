"""
题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
程序分析：直到找到不能再分解的因数，且相乘得输入数，直接程序退出（sys.exit()）
"""

import sys
def prime(num, copynum, strn, multi):
    for i in range(2, num):
        if num % i == 0:
            strn += '{}*'.format(i)
            multi *= i
            if multi == copynum:
                print(multi, '=', strn[:-1])
                sys.exit()
            num = num//i
            prime(num, copynum, strn, multi)
stanum = int(input('请输入一个整数：'))
prime(stanum, stanum, '', 1)
