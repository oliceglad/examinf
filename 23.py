
n = 25 
List = [0] * n 
List[3] = 1

for i in range(3, n):
    # Прибавить 1
    List[i] += List[i-1]
    # Четное
    if i % 2 == 0:
        List[i] += List[i//2]
    # Нечетное
    if i % 2 != 0:
        List[i] += List[(i-1)//2]

print(List[24])