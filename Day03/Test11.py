sum1 = 0
for i in range(1,101,1):        #range(开始值,最终值（不包含）,步长)；range(end)从0开始，到end-1结束，步长为1；range(start,end)从start开始，到end-1结束，步长为1
    if i % 2 != 0:
        sum1 += i
print(sum1)

sum2 = 0
for i in range(100,500,1):
    if i % 3 == 0:
        sum2 += i
print(sum2)
