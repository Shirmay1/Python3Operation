"""
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
程序分析：利用 while 或 for 语句,条件为输入的字符不为 '\n'。
"""

# 123runoobc  kdf235*(dfl
s = input('请输入一行字符(包含英文字母、空格、数字和其它字符):')
alpha, spac, dcima, other = [], [], [], []
for i in s:
    if i.isalpha():
        alpha.append(i)
    elif i.isspace():
        spac.append(i)
    elif i.isdecimal():
        dcima.append(i)
    else:
        other.append(i)
print('英文字母{}个，空格{}个，数字{}个，其它字符{}个'.format(len(alpha), len(spac), len(dcima), len(other)))


i, alpha, spac, dcima, other = 0, 0, 0, 0, 0
while i < len(s):
    if s[i].isalpha():
        alpha += 1
    elif s[i].isspace():
        spac += 1
    elif s[i].isdecimal():
        dcima += 1
    else:
        other += 1
    i += 1
print('英文字母{}个，空格{}个，数字{}个，其它字符{}个'.format(alpha, spac, dcima, other))
