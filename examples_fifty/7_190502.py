"""
题目：将一个列表的数据复制到另一个列表中。
"""
import copy
# 不可直接将列表赋给一个变量（如：list2=list1），这不是复制，而是引用，引用会带着原始列表一起改变，
list1 = [1, 3, 'hello', ('dog', 'cat')]
list2 = list1[:]
list3 = copy.copy(list1)
list4 = list1
list4[0] = '非复制而是引用'
print(list1)
print(list2)
print(list3)
print(list4)
