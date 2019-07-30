"""
一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
"""
heigh = []
sum_heigh = 0
hei = 100
for i in range(1, 11):
    if i == 1:
        sum_heigh = 100
    else:
        sum_heigh += hei*2
    hei /= 2
    heigh.append(hei)
print('总高度：', sum_heigh)
print('第10次反弹高度：', heigh[-1])

