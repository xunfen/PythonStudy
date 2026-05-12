num1 = input ("请输入第一个数字：")
num1 = int(num1)
num2 = input ("请输入第二个数字：")
num2 = int(num2)
choose = input ("请输入运算符号：")
match choose:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/' if num2 != 0:              # 判断除数是否为0,可以在case中排除条件
        print(num1 / num2)
    case _:
        print("输入错误")
