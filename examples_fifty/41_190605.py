"""模仿静态变量的用法。"""
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print(self.StaticVar)
print(Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()
