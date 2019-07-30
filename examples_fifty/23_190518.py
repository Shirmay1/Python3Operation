"""
打印出如下图案（菱形）
"""
lis_num = [1, 3, 5, 7, 5, 3, 1]
for i in lis_num:
    s = ' ' * (4-(i+1)//2) + i * '*'
    print(s)
