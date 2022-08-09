print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = (x <= (not y)) == (z or y)
            if f:
                print(x,y,z)