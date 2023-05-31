import os

# 查询工作路径 getcwd
# re = os.getcwd()
# print(re)
# 绝对路径
# r3 = os.path.abspath('demo9')
# print(r3)

# 添加文件夹 工作路径添加
# os.mkdir('image')
# os.mkdir('.vscode/image')

# 路径访问
r2 = os.listdir('.vscode')
# print(r2)


# 移除文件 需要权限
# os.mkdir('.vscode/image.py')
# os.remove('.vscode/image.py')

# 获得环境变量
# print(os.environ)

# 获取文件大小 单位为字节
path = './demo9/package/modu.py'
path1 = './demo9/package/modu'
path2 = './demo9/package'
r1 = os.path.getsize(path)
print(r1)

# 检测文件是否存在
print(os.path.isfile(path))
print(os.path.isfile(path1))

# 检测是否为路径
print(os.path.isdir(path))
print(os.path.isdir(path2))
