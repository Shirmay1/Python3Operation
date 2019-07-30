"""
求输入数字的平方，如果平方运算后小于 50 则退出。
"""
while True:
    num = int(input('请输入一个数：'))
    num = num ** 2
    if num < 50:
        break
        
