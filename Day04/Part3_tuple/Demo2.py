t1 = (80, 95, 78, 50, 76, 80, 85, 20)
print(t1)
print(type(t1))

#使用索引访问
print(t1[0])
print(t1[-1])

#切片
print(t1[0:5:1])


#count统计元素的个数
print(t1.count(80))


#index查找元素索引
print(t1.index(80))     #返回的是第一个元素出现的位置



t2 = (100)
print(type(t2))     #如果定义单元素的元组，必须加逗号，不然编译器会认为这是数字
t3 = (100,)
print(type(t3))