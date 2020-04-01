# Python-102 Exercise 3
# asking user for number in degree celsius
temp = input('Enter a temperature number in Celsius: ')

# converting answer to a integer
temp_num = int(temp)

#converting to fahrenheight
fahr_temp = ((temp_num * (9/5)) + 32)

#printing temp in fahrenheight
print(f'The temperature is {fahr_temp} degree Fahrenheight!')

