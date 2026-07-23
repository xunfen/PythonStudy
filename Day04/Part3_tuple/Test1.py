a = 10
b = 20

""" t1 = a, b
a = t1[1]
b = t1[0]

print(a)
print(b) """

a, b = b, a     #=右边相当于组包定义了一个元组，=左边相当于解包
print(a)
print(b)
