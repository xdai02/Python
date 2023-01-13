while True:
    info = input("Username:Password >>> ")

    if len(info) == 0 or info.find(":") == -1:
        print("输入格式错误！")
    else:
        data = info.split(":")
        username = data[0]
        password = data[1]
        if username == "admin" and password == "123456":
            print("欢迎【%s】成功登录！" % username)
            break
        else:
            print("用户名或密码错误！")