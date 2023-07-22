'''for i in range(1,21):
    if i % 2 == 0:
      print('i = {} is even'.format(i))
    else:
        print('i = {} is odd'.format(i)) '''
        
#working with floats
'''
my_float = input('Enter a decimal number with 5 deimal paces: ')
my_float = float(my_float)

print('Rounded up value is {:.2f}'.format(my_float))'''

#investment and interest 

'''
investment, interest = input('Enter invest amount and interest rate in float: ') .split()
investment = int(investment)
interest = float(interest)
for i in range(10):
    investment = investment + (investment * interest)
print ('Your investment in 10 years : {:.2f}'.format(investment)) '''


#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

# Extract the last digit of the number
last_digit = abs(number) % 10
if number < 0:
    last_digit *= -1

# Determine the message based on the last digit
if last_digit > 5:
    message = "and is greater than 5"
elif last_digit == 0:
    message = "and is 0"
else:
    message = "and is less than 6 and not 0"

# Print the result
print ('Last digit of {} is {} {}'.format(number, last_digit, message))
