"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""
week = {'M': 'Monday','T': {'u': 'Tuesday', 'h': 'Thursday'}, 'W': 'Wednesday', 'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
letter1 = input("请输入首字母：")
letter1 = letter1.upper()
if (letter1 in ['T','S']):
    letter2 = input("请输入第二个小写字母：")
    print(week[letter1][letter2])
else:
    print(week[letter1])
