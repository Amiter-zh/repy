# list 列表
# 变量 = [元素1，元素2，元素3，元素4，元素5]
# 一组数据的集合 数组？？？ arr?
heros = ['iron men', 'spider men', 'usa captain', 'black widow']
# print(type(heros))
# print(heros[3])

# py中可以四则表达式？去列表数据 1：3 取12 打印的结果也是列表形式
# 其实和循环中的range方法一致
# print(heros[1:3])
# print(heros[:3])
# print(heros[2:])
# print(heros[::2])

# 计算长度 len（） 同java中 .length
# print(len(heros))

# 增 append
# 追加元素 末尾添加
# .append()
heros.append('Doctor Strange')
print(heros)

# 删 remove pop
# 删除元素 末尾删除
# .pop() 可以指定位置删除
# heros.pop()
# print(heros)
# heros.pop(1)
# print(heros)
# 查询删除 remove
# remove是遍历列表 找到第一个完全相同的值然后进行删除 后续重复不变 不支持模糊
# heros.append('usa captaine')
# print(heros)
# heros.remove('usa captain')
# print(heros)

# 改 = insert
# 1.直接修改列表元素
# heros[1] = 'pig man'
# print(heros)
# 依照索引插入元素
# .insert()
# 其余元素后推
# heros.insert(1, 'spider men')
# print(heros)

# 查 index count in
# index 查询到元素返回索引值
# 如果不存在会报错
# 参考前置remove
n = heros.index('spider men')
print(n)
# count 查询列表中查询元素的数量
heros.append('iron men')
x = heros.count('iron men')
print(x)
# 解决查询报错 in
print('a' in heros)
print('a' not in heros)
print('iron men' in heros)

# len list的个数求解
print(heros)
print(len(heros))
