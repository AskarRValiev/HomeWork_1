wd = int(input('Enter the number of weekday '))

if wd < 1 or wd > 7:
    print('Wrong number!')
elif wd==6 or wd==7:
    print('It\'s holyday!')
else:
    print('It\'s not holyday')

    