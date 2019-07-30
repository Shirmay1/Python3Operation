"""
按逗号分隔列表。
"""
L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)


L = [1, 2, 3, 4, 5]
for i in L:
    if i == L[-1]:
        print(i, end='')
    else:
        print(i, end=',')
