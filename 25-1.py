# Маска(новая версия задачи 25)
from fnmatch import fnmatch


for i in range(352605, 10 ** 9):
    s = str(i)
    if int(i** 0.5)**2 == i and fnmatch(s, '352*6?5*'):
        print(i, i  ** 0.5 )

# --------------------------------------------------------
import fnmatch

mask = fnmatch.filter([str(x) for x in range(352605, 10 ** 8)], '352*6?5*')

for s in mask:
    x = int(s)
    if round(x ** 0.5) == x ** 0.5:
        print(x, x ** 2)

for num in range(1, 1000000):
    num = str(num)
    fl = False
    for i in range(len(num)-2):
        if num[i] == '6' and num[i+2] == '5':
            fl = True
    if fl:
        num = int('352'+num)
        if int(num **0.5)**2 == num:
            print(num, num ** 0.5)