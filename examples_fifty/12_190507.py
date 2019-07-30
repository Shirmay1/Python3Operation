"""
题目：判断101-200之间有多少个素数，并输出所有素数。
程序分析：一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数。 　　　　　
"""
for num in range(101, 201):
    lis = []
    for i in range(2, num):
        if num % i == 0:
            lis.append(i)
            break
    if len(lis) == 0:
        print(num)
