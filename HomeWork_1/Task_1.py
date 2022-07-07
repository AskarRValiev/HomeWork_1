wd = int(input('Enter the number of weekday '))
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
if wd < 1 or wd > 7:
    print('Wrong number!')
else:
    print(weekdays[wd-1])