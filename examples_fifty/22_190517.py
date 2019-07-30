"""
两个乒乓球队进行比赛，各出三人。
甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。
a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
lis1 = ['a', 'b', 'c']
lis2 = ['x', 'z', 'y']
for i in lis2:
    if i == 'x':
        for j in lis1:
            if j == 'a' or j == 'c':
                continue
            else:
                print('order is {}--{}'.format(i, j))
                lis1.remove(j)
    elif i == 'z':
        for j in lis1:
            if j == 'c':
                continue
            else:
                print('order is {}--{}'.format(i, j))
                lis1.remove(j)
    else:
        for j in lis1:
            print('order is {}--{}'.format(i, j))
