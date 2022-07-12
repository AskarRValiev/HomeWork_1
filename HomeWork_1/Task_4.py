quart = int(input('Enter number of quarter from 1 to 4: '))
if quart < 1 or quart > 4:
    print('Wrong number')
elif quart == 1:
    print('x from 0 to infinity, y from 0 to infinity')
elif quart == 2:
    print('x from 0 to negative infinity, y from 0 to infinity')
elif quart == 3:
     print('x from 0 to negative infinity, y from 0 to negative infinity')
else:
     print('x from 0 to infinity, y from 0 to negative infinity') 