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
investment, interest = input('Enter invest amount and interest rate in float: ') .split()
investment = int(investment)
interest = float(interest)
for i in range(10):
    investment = investment + (investment * interest)
print ('Your investment in 10 years : {:.2f}'.format(investment))