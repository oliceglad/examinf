# Найдите кол-во чисел кратных 19 и максимальное число.
f = open("E:\egepython\1 part/17.txt")
a = []

for x in f:
    x = int(x)
    a.append(x)

f.close()

count = 0
max_numb = 0

for i in range(len(a)):
    if a[i] % 19 == 0 and a[i] % 2 != 0 and a[i] % 3 != 0 and a[i] % 5 != 0:
        count += 1
        if a[i] > max_numb:
            max_numb = a[i]

print(count, max_numb)