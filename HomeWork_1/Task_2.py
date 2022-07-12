print('x y z result')
print('-------------')
for x in 0, 1:
    for y in 0,1:
        for z in 0,1:
            diz = not(x or y or z)
            con = not x and not y and not z
            print(x, y, z, diz == con) 