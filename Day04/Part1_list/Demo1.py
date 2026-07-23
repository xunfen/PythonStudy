s = [1, 2, 3, 4, 5, 1, 0.7, "abc", True]  #列表中可以存放任意数据类型，数据可以重复
print(s)
print(len(s))
print(type(s))
print()

#获取列表中的元素
print(s[0])         #正向索引从0开始，0代表第一个元素
print(s[-1])        #反向索引从-1开始，-1代表最后一个元素
print()

#修改元素
s[0] = "hello"
print(s)

#s[9] = "world"     #修改的值超过索引范围会报错
#print(s)
print()

#删除元素
del s[0]
print(s)
print()

#遍历列表
for i in s:
    print(i)        #遍历不用像Java，C一样数组名+索引