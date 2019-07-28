"""
日期：2019/7/26
editor:Shirmay1
题目：二分查找(两种方法，递归方式，循环方式)
算法要求：1.必须采用顺序存储结构。2.必须按关键字大小有序排列。
思路：首先，假设表中元素是按升序排列，将表中间位置记录的关键字与查找关键字比较，如果两者相等，则查找成功；
        否则利用中间位置记录将表分成前、后两个子表，
        如果中间位置记录的关键字大于查找关键字，则进一步查找前一子表，否则进一步查找后一子表。
        重复以上过程，直到找到满足条件的记录，使查找成功，或直到子表不存在为止，此时查找不成功。
"""
import random


# 递归方式：传入被查找列表，以及需要查找的数
def binary1(querynum, lis):
    mid = len(lis) // 2
    # 直到子表不存在为止，此时查找不成功
    if not lis:
        print('所查找的数{}不在该列表中'.format(querynum))
    elif querynum == lis[mid]:
        print('{}查找成功'.format(querynum))
    elif querynum < lis[mid]:
        binary1(querynum, lis[:mid])
    # elif querynum > lis[mid]:
    else:
        binary1(querynum, lis[mid+1:])


# 非递归方式：传入被查找列表，以及需要查找的数
def binary2(querynum, lis):
    while True:
        mid = len(lis) // 2
        # 直到子表不存在为止，此时查找不成功
        if not lis:
            print('所查找的数{}不在该列表中'.format(querynum))
            break
        elif querynum == lis[mid]:
            print('{}查找成功'.format(querynum))
            break
        elif querynum < lis[mid]:
            lis = lis[:mid]
            continue
        # elif querynum > lis[mid]:
        else:
            lis = lis[mid+1:]
            continue


list1 = list(range(1, 1000))  # 生成1到1000的列表
list2 = random.sample(list1, 21)  # 从列表1里面挑选21个随机不重复的数
list3 = sorted(list2)  # 按升序排序得到列表3
print('查找列表:', list3)
num = input('请输入要查找的整数：')
binary1(int(num), list3)
binary2(int(num), list3)
