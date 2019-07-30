"""
日期：2019/4/27
题目：企业发放的奖金根据利润提成。
利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""

# 直接if判断
def method1(I):
    profits = int(I)
    if profits <= 100000:
        bonus = 0.1 * profits
    elif 100000 < profits <= 200000:
        bonus = 0.1*100000 + 0.075*(profits-100000)
    elif 200000 < profits <= 400000:
        bonus = 0.1*100000 + 0.075*100000 + 0.05*(profits-200000)
    elif 400000 < profits <= 600000:
        bonus = 0.1*100000 + 0.075*100000 + 0.05*200000 + 0.03*(profits-400000)
    elif 600000 < profits <= 1000000:
        bonus = 0.1*100000 + 0.075*100000 + 0.05*200000 + 0.03*200000 + 0.015*(profits-600000)
    else:
        bonus = 0.1*100000 + 0.075*100000 + 0.05*200000 + 0.03*200000 + 0.015*400000 + 0.01*(profits-1000000)
    print('应发的奖金总数为：', bonus)


# 列表
def method2(I):
    profits = int(I)
    pro = [1000000, 600000, 400000, 200000, 100000, 0]
    rat = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    bon = 0
    for i in range(6):
        if profits > pro[i]:
            bon += (profits-pro[i]) * rat[i]
            profits = pro[i]
    print('应发的奖金总数为：', bon)


# 字典
def method3(I):
    pro = int(I)
    r = 0
    profile = {1000000: 0.01, 600000: 0.015, 400000: 0.03, 200000: 0.05, 100000: 0.075, 0: 0.1}
    for i in range(6):
        if pro > list(profile.keys())[i]:
            r += (pro-list(profile.keys())[i])*list(profile.values())[i]
            pro = list(profile.keys())[i]
    print(r)


II = input('请输入当月利润(元)：')
method1(II)
method2(II)
method3(II)
