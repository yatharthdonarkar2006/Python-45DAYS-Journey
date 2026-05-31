# Nested if Conditional statements in Python

# Nested if is a conditional statement which is used to check multiple conditions

# syntax:

"""
if condition:
    
    block of code
    
elif condition:
    
    block of code
    
    if condition:
        
        block of code
        
    elif condition:
        
        block of code
        
    else:
        
        block of code
else:
    
    block of code
"""

age = int(input("Enter your age : "))
citizen = input ("Are you Indian (Y/N) : ")

if (age >=18 ) :
    print("You are Eligible for Vote")
    
    if citizen.upper() == "Y" :
        print ("Your are Eligible")
        
    else :
        print("not Eligible")
        
else :
     print("not Eligible")
        
#OUTPUT
"""
Input : 19
Are you Indian (Y/N) : Y
You are Eligible for Vote
Your are Eligible

Input : 19
Are you Indian (Y/N) : N
You are Eligible for Vote
not Eligible

Input : 15
not Eligible
"""