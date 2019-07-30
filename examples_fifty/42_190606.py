"""学习使用auto定义变量的用法。"""
num = 2
def autofunc():
    num = 1
    print('internal block num = {}'.format(num))
    num += 1
for i in range(3):
    print('The num = {}'.format(num))
    num += 1
    autofunc()
