"""
使用lambda来创建匿名函数。
"""
m, n = eval(input('请输入两个数字，并以逗号分隔：'))
h = lambda x, y: x//y
print(h(m, n))

