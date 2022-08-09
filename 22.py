# сначала 2 а потом 5 Найти НАИБОЛЬШЕЕ x

for x in range(1, 500):
    copy = x
    a = 0
    b = 0 
    while x > 0:
        a += 1
        if x % 2 == 0:
            b += 1
        x //= 2
    if b == 2 and a == 5:
        print(copy)