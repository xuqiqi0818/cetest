class Person():
    # 属性：成员变量
    name = 'xuqiqi'
    age = 18
    # gf = 'jjj'

    def eat(self):
        print('今天杭州下雨111')
        self.gf = 'hi'

p = Person()
print(p.gf)
print(p.eat())