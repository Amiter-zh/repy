# 命名规范 小写字母 不要和内置模块冲突（sys random）
# 可以包含更多的函数 方法和类
# 使用模块 import from

# 获取文件位置 sys path
import sys
print(sys.path)
if __name__ == '__main__':
    print(__name__)

name = 'Harry'
age = 28


def fight(tool=None):
    if tool:
        print('A use '+tool + ' to complete B')
    else:
        print('fly!')


class Course:
    def __init__(self, name, c_list=[]):
        self.name = name
        self.c_list = []

    def add_course(self, c_name):
        if c_name:
            self.c_list.append(c_name)
            print('The course {} has been successfully added'.format(c_name))
        else:
            print('the course can not be empty')

    def remove_course(self, c_name):
        if c_name in self.c_list:
            if c_name:
                self.c_list.remove(c_name)
                print('The course {} has been successfully deleted'.format(c_name))
            else:
                print('the course can not be empty')
        else:
            print('The subject {} is not listed in the course schedule'.format(c_name))


# c = Course('ikun')
# c.add_course('sing')
# c.remove_course('sing')
