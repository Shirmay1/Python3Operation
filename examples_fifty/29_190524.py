"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
num = input('请输入一个不多于5位的正整数：')
print('该数是{}位数'.format(len(num)))
for i in range(1, len(num)+1):
    print(num[-i], end='')
