# 10. Simple Calculator
"""
Using functions create:
add()
subtract()
multiply()
divide()
Take two numbers and operator as input.
"""

num1 = (int(input(" Enter number 1 : ")))
num2 = (int(input(" Enter number 2 : ")))
operator = input("Enter Operator : ")

def add(num1, num2):
    return num1+num2

def sub(num1, num2):
    return num1-num2

def mul(num1, num2):
    return num1*num2

def div(num1, num2):
    return num1/num2

if(operator == "+") :
    print(add(num1, num2))
    
elif(operator == "-") :
    print(sub(num1, num2))
    
elif(operator == "*") :
    print(mul(num1, num2))
    
elif(operator == "/") :
    print(div(num1, num2))
    
else :
    print ("Invalid Inputs")