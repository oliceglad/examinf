# Минимальное произведение кратное 46, где разность индексов - 8
f = open('E://egepython/27 задание/2.txt')
N = int(f.readline())
a = [int(x) for x in f]
minn = float('inf')

for i in range(N):
    for j in range(i+1, i+8):
        if  j < N and a[i] * a[j] % 46 == 0 :
            if a[i] * a[j] < minn:
                minn = a[i] * a[j]

if minn == float('inf'): 
    print(-1); 
else: 
    print(minn) 
