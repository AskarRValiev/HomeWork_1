import math

print('Enter coordinates point A')
x1 = float(input('x = '))
y1 = float(input('y = '))
print('Enter coordinates point B:')
x2 = float(input('x = '))
y2 = float(input('y = '))

distance = round(math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 2)
print('Distance between A and B is: ', distance)
