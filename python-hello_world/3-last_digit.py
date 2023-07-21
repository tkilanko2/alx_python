#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number) % 10 > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, number % 10))
elif (number) % 10 == 0:
    printprint("Last digit of {} is {} and is o".format(number, number % 10))
else:
    print("Last digit of {} is {} and is ".format(number, number % 10))
    

