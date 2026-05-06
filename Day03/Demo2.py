username = input("请输入账号: ")
password = input("请输入密码: ")
if username != "admin" or password != "123456":
    print(f"用户{username}登录失败！")
else:
    print(f"用户{username}登录成功！")
