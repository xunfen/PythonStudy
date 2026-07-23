s = [54, 15, 75, 108, 23, 78, 75]
print(s)

s.append(188)  #往列表的尾部添加元素
print(s)

s.insert(2, 99) #在列表的指定位置添加元素
print(s)

s.remove(75)    #删除列表中指定的第一个匹配的元素
print(s)

e = s.pop(1)    #删除列表中指定位置的元素，并返回该元素
print(e)
print(s)

s.sort()        #对列表进行排序,默认升序排序
print(s)

s.reverse()     #对列表进行倒序
print(s)