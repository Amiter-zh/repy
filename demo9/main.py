# 导入模块
# impor 模块名称
# 使用方式： 模块名称.变量名称（函数、类）

# import modu
# print(modu.name)
# c = modu.Course('ikun')
# c.add_course('sing')
# c.remove_course('sing')

# 可以import  as
# as后面就是重命名
# import modu as md
# print(md.name)
# c = md.Course('ikun')
# c.add_course('sing')
# c.remove_course('sing')

# from import方法导入
# 这样就是只导入模块中我们所需要的成员
# 并且调用可以直接调用无需前缀
# 如果向在一个模块中导入多个变量 可以使用 ，
# 导入全部就是 *
# from modu import Course
# from modu import name
from package.modu import *
print(name)
c = Course('ikun')
c.add_course('sing')
c.remove_course('sing')
