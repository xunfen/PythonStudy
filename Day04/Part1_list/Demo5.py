num_list1 = [19, 23, 45, 67, 89, 90]
num_list2 = [55, 19, 23, 123, 45, 67, 89, 90]

#合并列表
for i in num_list2:
    num_list1.append(i)
    
print(num_list1)

#简化合并列表
#解包：将列表这一类容器拆开成为一个一个独立的元素
#组包：将多个元素组合成一个容器
nenew_list = [*num_list1, *num_list2]
print(nenew_list)


#去除重复元素
new_list = []
for i in num_list1:
#    if i in new_list:   #判断i是否在new_list中,如果存在返回True,不存在返回False
    if i not in new_list:   #与上一行相反
        new_list.append(i)

print(new_list)