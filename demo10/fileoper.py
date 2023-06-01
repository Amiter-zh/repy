# open 系统内置 打开文件
# '存储位置/文件名字'
# 相对路径 相对于你当前文件的路径 ./demo10/main.py
# 绝对路径 E://pyt//demo10//main.py
import csv
import os

# path = os.getcwd()
# print(path)
# str = open('E://pyt//demo10//main.py')
# str = open('./demo10/main.py')

# mode
# r read
# w write 会自动判断文件是否存在 如果不存在会帮我们自动创建一个文件 w会覆盖
# a append 写入新数据不会换行 换行符也是字符
# t text
# b byte
# str = open('./demo10/main.py', mode='w')
# str = open('./demo10/ts.txt', mode='a', encoding='utf-8')
# print(str)

# recode = "print('AFK')"
# # write 写入数据 写完之后必须调用close关闭通道
# str.write(recode)
# str.close()

# recodes = ['AFC', 'KDC', 'AWDIUH', 'AWIKDH', 'OOK', 'DKK']
# STR = open('./demo10/ts.txt', mode='w')
# for i in recodes:
#     STR.write(i + '\n')

# STR.close()

# 读取 read()
# STR = open('./demo10/ts.txt')
# content = STR.read()
# print(content)
# STR.close()

# read 如果出现文件不存在会报错
# 报错处理try catch
# 一般在try之前open（） 在fin中close（）
# try:
#  可能错误代码
# except:
#   出现异常显示的代码
# finally:
# 	无论如何都会执行的代码
# try:
#     STR = open('./demo10/ts1.txt')
#     content = STR.read()
#     print(content)
#     STR.close()
# except:
#     print('error')
# finally:
#     print('over')

# 可以是使用with语句
# 可以看作是try-finally的简写形式 更加智能化
# with 语句是一种上下文管理器，用于自动管理资源的获取和释放。它的语法形式是 with expression as target:，在代码块结束时，无论是否发生异常，都会自动调用上下文管理器的 __exit__() 方法来释放资源。
# 简而言之就是不需要调用close函数关闭通路
# with context as 变量:
#     语句

# try:
#     with open('./demo10/ts1.txt') as str:
#         content = str.read()
#         print(content)
# except:
#     print('dd')

# 在这种情况下，with 语句用于自动关闭文件，并且 try-except 语句用于捕获可能的文件操作异常。

recodes = [['AFC', '10-12', 'RC'],
           ['KDC', '96-4 ', 'A'],
           ['AWDIUH', '74-9 ', 'DCX'],
           ['AWIKDH', '41-4 ', 'HBW'],
           ['OOK', '39-41', 'DHB'],
           ['DKK', '31-14', 'odi']]

# csv文件 行以换行符为分隔 每行又以都好分割 写入
# with open('./demo10/ts.csv', mode='w', encoding='utf-8') as str:
#     write = csv.writer(str)
#     write.writerow(['RED', 'SCORE', 'BLUE'])
#     # 单行写入 writerow
#     # for recode in recodes:
#     #     write.writerow(recode)
#     # 多行直接写入 writerows
#     write.writerows(recodes)

# csv读取
# with open('./demo10/ts.csv', mode='r', encoding='utf-8') as str:
#     reader = csv.reader(str)
#     for row in reader:
#         print(row)
