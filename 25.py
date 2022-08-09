# Найдите такие числа, где кол-во делителей равно 6
def func(numb):

    maxDel = 0
    countDel = 0

    for i in range(2,numb):
        if numb % i == 0:
            countDel += 1
            maxDel = i

    if countDel == 6:
        return maxDel
            
for i in range(192, 237+1):
    if func(i) != None:
        print(i, func(i))

# Найдите такие числа, где кол-во делителей равно 3
def func(numb):

    maxDel = 0
    countDel = 0

    for i in range(2,numb):
        if numb % i == 0:
            countDel += 1
            maxDel = i

    if countDel == 3:
        return maxDel
            
for i in range(14587, 20598+1):
    if func(i) != None:
        print(i, func(i))

# Найдите такие числа, где сумма делителей больше самого числа
def func(numb):
    summ = 0
    maxDel = 0
    for i in range(2,numb):
        if numb % i == 0:
            summ += i
            if i > maxDel:
                maxDel = i
    if summ > numb:
        return maxDel

for i in range(574, 612+1):
    if func(i) != None:
        print(i,func(i)) 


# Найдите кубы чисел
for i in range(1,1000+1):
    if 781456 <= i ** 3 <= 1495235:
        print(i**3, i)

# Простые числа
def is_prime(x):
    for i in range(2, round(x ** 0.5)+1):
        if x % i == 0:
            return False
    
    return True


for i in 3,5,8,11:
    if is_prime(i):
        print(i, "Простое число")