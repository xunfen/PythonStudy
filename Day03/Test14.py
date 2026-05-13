import random
random_number = random.randint(1, 100)
while True:
    num = input("请输入数字：")
    num = int(num)
    if num > random_number:
        print("猜大了")
    elif num < random_number:
        print("猜小了")
    else:
        print("猜对了!!!!!!!!!!!!!!!!")
        break
