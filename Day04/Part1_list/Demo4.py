num_list = []
for i in range(10):
    num = int(input("请输入数字："))
    num_list.append(num)

print(num_list)

num_list.sort()
print(num_list)

print(f"最小值为：{num_list[0]}")
print(f"最大值为：{num_list[-1]}")
#使用py自带的方法取最小值最大值
print("最小值为：" + str(min(num_list)))
print("最大值为：" + str(max(num_list)))

print(f"平均值为：{sum(num_list)/len(num_list)}")   #sum()求和,len()求长度/元素的个数,这是list的方法
