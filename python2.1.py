#py102, 1st exercise
# Prompting user for a num to determine what day of the week it is
day = input('Day of Week (0-6): ')

#converting string to integer
day_num = int(day)

#printing day of week
if day_num == 0:
    print('Its Sunday')
elif day_num == 1:
    print('Its Monday')
elif day_num == 2:
    print('Its Tuesday')
elif day_num == 3:
    print('Its Wednesday')
elif day_num == 4:
    print('Its Thursday')
elif day_num == 5:
    print('Its Friday')
else:
    print('Its Saturday! Lets Party!')

