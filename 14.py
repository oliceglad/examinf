# Система счисления
x = 625 ** 25 + 25 ** 50 - 5 ** 9 - 619
n = 5 
d = 4 

count = 0

while x > 0:
    a = x % n 
    x //= n 
    if a == d:
        count += 1

print(count)