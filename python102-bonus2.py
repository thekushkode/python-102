# python-102 bonus #2

# asking user to enter a number.
user_num_str = input('Guess a number between 0-10: ')

#changing answer to integer
user_num = int(user_num_str)


#imorts seed and random modules
from random import seed
from random import randint

#generating random number
comp_num = randint(0,10)
print(comp_num)
#checking to see if num picked equals random and displaying msg
for i in range(4):
    if user_num == comp_num:
        print('You won!')
        break
    else:
        print('Guess again!')
        user_num = input('Guess a number between 0-10: ')
        user_num = int(user_num)
        i += 1

