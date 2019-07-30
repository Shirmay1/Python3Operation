"""
两个变量值互换
"""
def exchange(a, b):
    a, b = b, a
    print('a：{}，b:{}'.format(a, b))
exchange(1, 'hello')
