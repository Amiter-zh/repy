# param n: 数量
# param kind: 种类
def milk_tea(n, kind='yukino', price=15):
    for i in range(n):
        print('正在制作第{}杯'.format(i+1))
        print('正在制作{}'.format(kind))
    print('应付{}元'.format(n*price))
    return '欢迎下次光临'


# milk_tea(3, 'aimer')
# milk_tea(1)
# 可以关键词传参 不用依照传参顺序
x = milk_tea(price=35, n=3)
print(x)
