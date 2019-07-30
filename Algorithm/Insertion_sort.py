"""
日期：2019/7/30
editor：Shirmay1
题目：插入排序
思路：插入排序算法的原理如下：
    先定义一个有序队列，然后把无序队列中的第一个元素放到有序队列的合适位置，重复操作，直至形成一个完整的有序队列。
"""
import random


def insertion_sort(lis):
    leng = len(lis)
    for i in range(leng):
        key = lis[i]
        j = i - 1
        while j >= 0 and key < lis[j]:
            lis[j + 1] = lis[j]
            j -= 1
        lis[j + 1] = key
        print('第{}次比较:'.format(i+1), lis)
    print('选择排序后的列表：', lis)


list1 = list(range(1, 100))  # 生成1到100的列表
list2 = random.sample(list1, 21)  # 从列表1里面挑选21个随机不重复的数
print('需被排序的列表:', list2)
insertion_sort(list2)
