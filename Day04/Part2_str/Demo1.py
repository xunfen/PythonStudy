s = "Hello World"
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])


#切片
print(s[0:5:1])   #不包含结束索引，要+1
print(s[:5:1])
print(s[:5:])
#开始索引 ： 结束索引 ： 步长
print(s[6:12:1])