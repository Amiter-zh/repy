#  for var in list:
# 		cir
# for x in range(5):
# range单一参数是从0到参数减一 这也是最核心的 两个参数的话就是从第一个参数开始到第二个参数-1 如果输入三个参数 就是隔x 一般只能一二参数只能正序，如果想倒叙需要第三个参数为负数
# print('num:', x)
# print('num:{}'.format(x))
# 区别 part1 是num和x之间存在一个分隔符 part2是调用了format（）方法 {}只是一个占位符 再将x填充到{}中

# for x in range(11, 2, - 1):
#     print('num', x)

# for x in range(2, 11, 2):
#     print('num', x)

# for x in range(3):
#     username = input('请输入用户名')
#     passward = input('请输入密码')
#     if username == 'admin' and passward == '123':
#         print('成功')
#         break
#     else:
#         print('失败')

# break and continue
# break 跳出循环
# continue 跳出该次循环
# for x in range(8):
#     if x == 3:
#         continue
#     print(x)

# python中 while for 和if都可以接else 表示 不成立时输出else
for x in range(8):
    print(x)
else:
    print('out')
