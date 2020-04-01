# Python-102 exercise 2
# Prompting user for a num to determine what day of the week it is
day = input('Day of Week (0-6): ')

#converting string to integer
day_num = int(day)

#determining day of week and giving corresponding msg
if day_num < 6 and day_num > 0:
    print('Go to work & get that paper!')
else:
    print('Get some R&R! zzzz...')