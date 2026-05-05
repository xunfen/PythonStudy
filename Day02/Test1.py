total = 10000
pwd = input("请输入密码：")
money = input("请输入取款金额：")
print(money + "取款成功！,目前还剩余" + str(total - int(money)) + "元")