str = "   -aBcDeFg-123456-aBcD-   "

print(str.find("c"))    #查找字符串中的子串，找不到返回-1
print(str.find("cD"))

print(str.count("c"))   # 统计子串出现的次数
print(str.count("6"))


new_str = str.upper()   # 转大写
print(new_str)

new_str = str.lower()   # 转小写
print(new_str)

str_list =str.split("-")  # 字符串分割
print(str_list)

new_str = str.strip()   # 去掉字符串头尾的指定字符
print(new_str)

new_str = str.replace("-",",")  # 替换字符串,后者替换前者
print(new_str)

#判断字符串是否以某字符开头或结尾
print(str.startswith("-"))
print(str.endswith("-"))