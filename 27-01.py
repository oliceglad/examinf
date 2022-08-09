# Кольцевая дорога, решение на 2 балла

f = open('fileA1.txt')
n = int(f.readline())
apple = []

for i in range(n):
    apple.append(int(f.readline()))
f.close()

s = [0] * n

# s[0]
for j in range(n):
    way1 = j
    way2 = n-j
    s[0] += apple[j] * min(way1,way2)
min_sum = s[0]
# Ps[0]
Ps = [0] * n

for i in range(n//2):
    Ps[0] += apple[i]

# Ps[i]

for i in range(1,n):
    # Процент n, для того чтобы не выходить за границы окружности
    Ps[i] = Ps[i-1] - apple[i-1] + apple[(i-1+n//2)%n] 

# s[i]

for i in range(1,n):
    s[i] = s[i-1] - Ps[i] + Ps[(i+n//2)%n]
    if s[i] < min_sum:
        min_sum = s[i]

print(min_sum)










