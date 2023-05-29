# 字符串
# ''  ""  ''' '''  都是合法字符串
# '' ""主要是用来混搭 '''''' 可以保留格式
message = 'awdiugauywdg'

print(message[1])
print(message[1:6])

# .find() 查找位置 find找不到会返回-1 index则会报错
# 所以一般使用find
print(message.find('wdg'))
print(message.index('wdg'))
print(message.find('wdg1'))
# print(message.index('wdg1'))

# .startswith()判断是否以（）开头 .endswith()结尾 返回布尔型
print(message.startswith('aw'))
print(message.startswith('di'))

# .strip() 去掉空白符和制表符
x = "        awdhbhuiaw@#awdikuhiu\t\t\n"
print(x)
print(x.strip())

# str长度 len
print(len(x))
print(len(x.strip()))
