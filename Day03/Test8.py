a = input("请输入第一条边：")
b = input("请输入第二条边：")
c = input("请输入第三条边：")
a = int(a)
b = int(b)
c = int(c)
if a + b > c and a + c > b and b + c > a:
    #print("是三角形")
    if a == b and b == c:
        print("等边三角形")
    elif a==b or b==c or a==c:
        print("等腰三角形")
    else:
        print("普通三角形")
else:
    print("不是三角形")
