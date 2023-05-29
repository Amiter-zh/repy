# dictionary 字典
# 变量 = {key1:value1,key2:value2,key3:value3,key4:value4}\
# 类似java中类的各个成员变量
hero = {'name': 'iron man', 'ability': 'money', 'power': 'technology'}
print(type(hero))

# 数据获取 类似列表 但需要key
print(hero['name'])
print(hero['ability'])
# 不存在的key会报错
# 解决方法 .get()
# 不存在会返回none 也可以自定义
print(hero.get('ddd', 'can`t find'))
print(hero.get('power', 'can`t find'))

# 增 =
hero['IQ'] = 150  # type: ignore
print(hero)
hero['blood'] = 30000  # type: ignore
print(hero)

# 删除 pop 用法类似列表 但是列表输入的是元素位置 字典则是key
# 依旧是如果不存在会报错
# hero.pop('IQ')
# print(hero)

# 查：in
print('IQ' in hero)
print('blood' in hero)
# 判断key存不存在 不可以判断value存不存在
# 采用.values()可以将字典中的所有value输出，变成一个列表 在判断存不存在value
# 注意类型不同也无法查询到
print(hero.values())
print(30000 in hero.values())

# 改 类似增
hero['IQ'] = 1050  # type: ignore

# 存在多少个键值对
print(hero)
print(len(hero))
