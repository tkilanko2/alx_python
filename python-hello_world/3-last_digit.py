#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE

# Check the value of the last digit and print the result
if str(number)[-1] > '5':
    print("Last digit of {} is {} and is greater than 5".format(number, str(number)[-1]))
elif str(number)[-1] == '0':
    print("Last digit of {} is {} and is 0".format(number, str(number)[-1]))
else:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, str(number)[-1]))
