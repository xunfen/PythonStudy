username = input("请输入账号: ")
password = input("请输入密码: ")
if username == "admin" and password == "666888":
    print(f"用户{username}登录成功！")
elif username == "root" and password == "547527":
    print(f"用户{username}登录成功！")
elif username == "zhangsan" and password == "123456":
    print(f"用户{username}登录成功！")
else:
    print("登录失败！请检查账号密码！")