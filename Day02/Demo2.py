slogan1 = "Hello" "World"
print(slogan1)

slogan2 = "Hello" + "World"
print(slogan2)

s1 = "人生苦短"
s2 = "我用Python"
print(s1 + s2)

#字符串拼接
print("===========================")
name  = "小汪"
age = 18
pro = "软件工程"
hobby = "python"
print("我叫" + name + "，今年" + str(age) + "岁，专业是" + pro + "，爱好是" + hobby)    #int类型不能直接被拼接，要用str()函数转成字符串

#字符串格式化
print("===========================")
print("我叫%s，今年%d岁，专业是%s，爱好是%s" % (name, age, pro, hobby)) #和C语言要用

#字符串格式化2
print("===========================")
#格式：f"内容{变量/表达式}"
print(f"我叫{name}，今年{age}岁，专业是{pro}，爱好是{hobby}")
