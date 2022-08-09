# Самый встречающийся символ в файле
d = {}
f = open("E:/egepython/3.txt")
x = f.read()

maxx = 0

for i in range(len(x)):
    if x[i] in d.keys():
        d[x[i]] += 1
    else:
        d[x[i]] = 1

for key in d.keys():
    if d[key] > maxx:
        maxx = d[key]

print(key,maxx)