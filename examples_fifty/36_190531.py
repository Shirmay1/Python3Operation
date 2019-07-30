"""
求100之内的素数。
"""
for num in range(2, 100):
    lis = []
    for i in range(2, num):
        if num % i == 0:
            lis.append(i)
            break
    if len(lis) == 0:
        print(num)
