money1 = 10
money2 = 20
# 数据类型主要是用来进行运算
print(money1+money2)
print(money1-money2)
print(money1*money2)

# 运算 1.优先级 2.从左到右
print((100-41)*2-88/4)

# 赋值运算从右向左

# 字符串相加等于拼接
name = '帕朵'
name2 = '菲利斯'
print(name + name2)
# str 和int是无法连接的，所以我们需要类型转换
age = 18
print(name + name2 +str(age))
# 类型转换方式
# int - float  int（） float（） float=》int 会舍弃小数位
# print(int(name))
# 报错ValueError: invalid literal for int() with base 10: '帕朵'
# 分析原因 str如果是字符是不能强转为int的 并且如果字符串结构是float同样也不能强转为int
# 结论 str字符类型不能转为float和int类型 具有浮点结构的str也不能转换为int类型
