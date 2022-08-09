# Максималньое произведение чисел кратное 62, решение на 2 балла
f = open("E://egepython/27 python/2.txt")
n = int(f.readline())
a = [int(i) for i in f]
m62_1 = m62_2 = m31 = m2 = m0 = 0

for i in range(n):
    x = a[i]
    if x % 62 == 0:
        if x > m62_1:
            m62_1 = x
            m62_2 = m62_1
    elif x % 2 == 0:
        if x > m2:
            m2 = x
    elif x % 31 == 0:
        if x > m31:
            m31 = x
    else: 
        if x > m0:
            m0 = x

pr = max(m62_1 * m62_2, m31 * m2, m62_1 * m31, m62_1 * m2 )

print(pr)