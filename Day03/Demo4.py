day = input ("请输入星期几：")
match day:
    case "1":
        print("星期一")
    case "2":
        print("星期二")
    case "3":
        print("星期三")
    case "4":
        print("星期四")
    case "5":
        print("星期五")
    case "6" | "7":
        print("周末")
    case _:                 #表示匹配所有情况，相当于switch中的default
        print("输入错误")

