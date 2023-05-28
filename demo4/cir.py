# 循环 节约代码量
o = 3
# while o > 0:
# 	print('kfcv050',o,sep='`')
#     o -= 1
while o >= 1:
    username = input('请输入用户名')
    passward = input('请输入密码')
    if username == 'admin' and passward == '123':
        print('成功')
        break
    else:
        if o != 1:
            print('请重新输入')
            o -= 1
        else:
            print('没有次数了！')
            break
