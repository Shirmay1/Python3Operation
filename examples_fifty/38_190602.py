"""
求一个3*3矩阵主对角线元素之和。
"""
lis = []
sum_lis = 0
for i in range(3):
    a = []
    for j in range(3):
        a.append(int(input('请输入一个数：')))
    lis.append(a)
    sum_lis += lis[i][i]
print('3*3矩阵为：', lis)
print('3*3矩阵主对角线元素之和为：', sum_lis)
