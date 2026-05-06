year = input("请输入年份：")
year = int(year)    #input获取到的数据都是字符串类型，需要转换成int类型
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("闰年")
else:
    print("平年")