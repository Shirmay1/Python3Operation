"""
日期：2019/7/25
editor：Shirmay1
题目：冒泡排序（两种循环方法）
思路：冒泡排序算法的原理如下：
    比较相邻的元素。如果第一个比第二个大，就交换他们两个。
    对每一对相邻元素做同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
"""
import random


def bubble2(lis):
    leng = len(lis)
    # move = 0
    # while move != 0:
    while lis != sorted(lis):
        for i in range(leng-1):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
                # move = 1
            else:
                continue
    print('冒泡排序后的列表：', lis)


def bubble1(lis):
    leng = len(lis)
    for i in range(leng - 1):
        move = 0
        for j in range(leng - 1):
            if lis[j] > lis[j + 1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
                move += 1
            else:
                continue
        print('第{}次比较:'.format(i+1), lis)
        # if lis == sorted(lis):
        #     break
        if move == 0:
            break
    print('冒泡排序后的列表：', lis)


list1 = list(range(1, 100))  # 生成1到100的列表
list2 = random.sample(list1, 21)  # 从列表1里面挑选21个随机不重复的数
print('需被排序的列表:', list2)
bubble1(list2)
bubble2(list2)
