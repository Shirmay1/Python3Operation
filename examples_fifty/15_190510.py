"""
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
程序分析：程序分析：(a>b)?a:b这是条件运算符的基本例子。：
"""

def judge(scor):
    if scor >= 90:
        per = 'A'
    elif scor >= 60:
        per = 'B'
    else:
        per = 'C'
    print('{}分的同学等级为{}'.format(scor, per))
score = input('请输入分数：')
judge(int(score))
