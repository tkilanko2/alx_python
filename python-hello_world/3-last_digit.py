#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# Calculate the last digit of the number with its sign intact

# Check the value of the last digit and print the result
print('{}'.format(number))
last_digit = str(number)[-1]
if last_digit > '5':
    print("Last digit of {} is {} and is greater than 5".format(number,last_digit ))
elif last_digit == '0':
    print("Last digit of {} is {} and is 0".format(number,str(number)[-1] ))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_digit ))