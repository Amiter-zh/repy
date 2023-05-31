# from modu import *
# print("succ")

from datetime import *
import random as r
import time as t

t1 = t.time()
print(t1)
# ctime 将time转换为可视化时间
print(t.ctime(t1))

# for i in range(5):
#     print(i)
#     t.sleep(1)

print(datetime.now())

dt = datetime.now()
# timedelta时间差
dt1 = dt + timedelta(days=-1)
print(dt1)

# random
# random() 随机生成0-1直接的数
# randint（） 随机生成范围内的int整数
# randrange（） 随机生成整数不包括后项

print(r.random())
print(r.randint(1, 5))
print(r.randrange(1, 9))
names = ['A', 'B', 'C', 'D', 'E']
print(r.choice(names))
