a = 1
sum = 0
while a <= 100:
    if a % 2 == 0:
        sum = sum + a
    a = a + 1
print(f"100内偶数的和{sum}")