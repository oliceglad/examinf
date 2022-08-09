# Один из типов 15 задачи
for A in range(0, 500):
    flag = True 
    for x in range(0,500):
        for y in range(0,500):
            F = ((x * x <= A) or (x > 7 )) and ((y * y <= A) <= (y <= 7))
            if not F:
                flag = False
                break
        if not flag:
            break
    if F:
        print(A)