"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""
num = input('请输入一个五位数：')
if num[0] == num[-1] and num[1] == num[-2]:
    print('{}是回文数。'.format(num))
else:
    print('{}不是回文数。'.format(num))
