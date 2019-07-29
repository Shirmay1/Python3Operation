"""
日期：2019/7/29
editor：Shirmay1
题目：选择排序
思路：选择排序算法的原理如下：
    从待排序列中选出最小（或最大）的一个元素，记录其下标的位置；
    将记录的下标值与待排序列的第一个元素进行交换；
    以此类推，直到全部待排序列的元素排完。
"""
import random


def select(lis):
    leng = len(lis)
    for i in range(leng):
        min_idx = i
        for j in range(i + 1, leng):
            if lis[min_idx] > lis[j]:
                min_idx = j
        lis[i], lis[min_idx] = lis[min_idx], lis[i]
        print('第{}次比较:'.format(i+1), lis)
    print('选择排序后的列表：', lis)


list1 = list(range(1, 100))  # 生成1到100的列表
list2 = random.sample(list1, 21)  # 从列表1里面挑选21个随机不重复的数
print('需被排序的列表:', list2)
select(list2)
