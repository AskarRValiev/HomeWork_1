print('Enter coordinates x > 0, y > 0')
x = int(input('x = '))
y = int(input('y = '))
if x == 0 or y == 0:
    print('Wrong data')
elif x > 0 and y > 0:
    print('I quarter')
elif x < 0 and y > 0:
    print('II quarter')
elif x <0 and y < 0:
    print('III quarter')
else:
    print('IV quarter') 