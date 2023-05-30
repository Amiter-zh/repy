# fuction 队某一特定功能的封装 打包
# def {name} (para ,默认参数):
# 	函数体
# 包括两种 有参数以及无参数 有参数必须传参且按照声明方式传参
# 默认参数就是参数默认传递一个值,这个参数可以不填写 不填写采用默认值
def heros(n):
    for i in range(n):
        print('i')
        print('do')
        print('not')
        print('to')
        print('study')
        print('----------------------')


def hero():
    print('=======================')
    print('i')
    print('do')
    print('not')
    print('to')
    print('study')


#   函数调用：函数名（参数）
hero()
heros(3)
