"""
对10个数进行排序。
"""
# 方法一：
a = input('请输入10个数字，以英文逗号分开：')
split_lis = a.split(',')
split_lis.sort()
print(split_lis)

# 方法二：
b = list()
for i in range(10):
    b.append(int(input('请输入一个数字：')))
b.sort()
print(b)
