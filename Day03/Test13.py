while True:
    username = input("请输入用户名: ")
    password = input("请输入密码: ")
    if username == "" or password == "":
        print("用户名或密码不能为空！")
        continue                                            #continue:跳过本次循环,进行下一次循环

    if username == "admin" and password == "666888":
        print("登录成功！")
        break                                               #break:跳出循环
    elif username == "zhangsan" and password == "123456":
        print("登录成功！")
        break
    elif username == "lisi" and password == "654321":
        print("登录成功！")
        break
    else:
        print("登录失败！请检查账号密码！")