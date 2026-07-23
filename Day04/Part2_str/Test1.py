mail = input("请输入你的邮箱: ")
if "."  not in mail:
    print("邮箱格式错误")
elif mail.count("@") != 1:
    print("邮箱格式错误")
else:
    print("邮箱格式正确")