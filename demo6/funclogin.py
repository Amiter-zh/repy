def login():
    username = input('请输入用户名')
    password = input('请输入密码')
    print(type(password))
    # 这边input中写入的str类型 所以后续判断中 password也需要str类型
    if username == 'admin' and password == '123':
        print('login in')
    else:
        print('login fail')


login()
