#simple calculator
print('''
note that expression must contain Addition,Substraction,Product,Division only
example :
output ->Enter the expression 
      9+1-9*8-8*8*8*8
      =-4158
''')
import math
x=input("Enter the expression \n")
print(eval(x))