# if-else is a conditional Statement

#if and else keyword is used

# if condition is true then block of code under if statement will be executed if condition is false then block of code under else statement will be executed

"""
 syntax:
 
 if condition:
     
     block of code
     
 else:
     
     block of code
"""

age = (int(input("Enter Your Age : ")))

if (age >= 18):
    print("You are Eligible for Vote")
    
else:
    print("You are not Eligible for Vote")


#OUTPUT

"""
Input : 19
You are Eligible for Vote

Input : 15
You are not Eligible for Vote
"""