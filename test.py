#Also found a UI/UX person and a couple of questions popped up about 
"""the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!") """

'''name = "Tolulope Kilanko"
lenght = len(name)
product = "Iphone"
price = 1000
height = 176.78
bra_size = 17j
#rep = name.replace("Tolulope", "Gideon")

"""print("My name is:" + name)
print("I bought an:" + product)
print("It cost me:" + str(price))"""

#print("My name has" , str(lenght) , "characters")
#print("{1} has {0} characters" .format(rep,lenght))
#print("{0} bought his {1} for {2}" .format( name, product, str(price) ))
'''

'''name = input("Please enter your name: ")
age = input("Please enter your age: ")
print("Hello", name)
print("You are {} years old".format(age))'''

#name = "Jide"
'''lenght = float(input("Please enter the lenght of your room in feets:")) 
width = float(input("Please enter the with of your room in feets:"))
area = lenght * width

#print("The area of your room is {}ft".format(area))'''
#print("I love this {}".format(name[-1]))

'''
height, width = input('Enter 2 numbers in fts') .split()
height = int(height)
width = int(width)

sum = height + width
product = height * width
remainder = height % width
division = height / width
rounded_up_devide = height // width

print("Sum of {} + {} is {}".format(height, width, sum)) '''

#to convert miles to kilometers

#allow users to input 2 numbers with an operation and give the result 

'''
num1, operator, num2 = input('Enter calculation') .split()
num1 = int(num1)
num2 = int(num2)

#calculation
if operator == "+":
    print("{} + {} = {}".format(num1, num2, num1+num2))
elif operator == "-":
        print("{} - {} = {}".format(num1, num2, num1-num2))
elif operator == "*":
        print("{} * {} = {}".format(num1, num2, num1*num2))
elif operator == "/":
        print("{} / {} = {}".format(num1, num2, num1/num2))
else:
    print('Use any of the following operators: +, -, / or *')  '''
    
    
#different output based on age

'''
age = eval(input("Enter your age:")) 

if age >= 1 and age <= 18:
    print('You are {} years old, your age is important'.format(age))
elif age == 21 or age ==50 or age == 65:
    print('You are {} years old, your age is important'.format(age))
else:
    print('You are {}, your age is not important'.format(age)) '''
    
    
    #age and kindagerten 
'''age = eval(input("Enter your age:")) 

if age == 5:
    print('You are {} years old, go to Kindergarten'.format(age))
elif age >= 6 and age <= 17:
    grade = age - 5
    print('You are {} years old, go to grade {}'.format(age, grade))
elif age == 17:
    print('You are {} years old, go to College'.format(age))
else:
    print('You are {}, no luck for you'.format(age))  '''

def my_function():
     print("In my functions")
 
my_function