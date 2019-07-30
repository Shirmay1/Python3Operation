"""
求1+2!+3!+...+20!的和。
"""
sum = 0
t = 1
for n in range(1, 21):
    t *= n
    sum += t
print('1+2!+3!+...+20!={}'.format(sum))
