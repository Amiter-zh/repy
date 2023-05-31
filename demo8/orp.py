# class 类名：
# 	属性
# 	方法
# 1.类名首字母大写
# 2. 类型后面有冒号
# 3. 类体有缩进

class Phone:
    brand = 'huawei'
    color = 'black'
    type = 'Mate 30'
    price = 3999

    def call(self):
        print('call')

    def send_message(self):
        print('take the message')


class Saiya:
    name = 'goku'
    hair = 'fixed'
    has_tail = True
    appetite = 'big'

    def fight(self):
        print('ready fight')


# 对象创建
# 对项目 = 类名（参数）
Phone1 = Phone()
Phone2 = Phone()
Phone3 = Phone()

# print address different
# # obj different
# print(Phone1)
# print(Phone2)
# print(Phone3)

# 如何访问
# 对象名.方法名（）/属性名
# print(Phone1.brand)
# Phone1.send_message()

# s1 = Saiya()
# s1.fight()
# print(s1.name)

# 对象属性的重新赋值
# 1. 动态添加
# 2. 创造对象时 ，__init__添加

print(Phone1.brand)
Phone1.brand = 'oppo'
print(Phone1.brand)


class Person:
    country = 'China'

    def __init__(self, name):
        print('init method')
        # self 对象本身
        print(self)
        self.name = name

    def eat(self):
        print(self.name + ' eater')

    def sport(self, time):
        if time < 6:
            print(self.name + ' fight')
        else:
            print(self.name+' lazy dog')

        self.eat()


p1 = Person(name='aicy')
p2 = Person(name='goku')
p1.sport(3)
p2.sport(9)

# 继承 (Inheritance)
# 类名（继承类）


class superP(Person):
    def fight(self):
        print('ready fight')


s = superP('JPD')
s.fight()
s.sport(5)
