# if-elif-else conditional statements in Python

# if-elif-else is a conditional statement

# if, elif and else keyword is used

# if condition is true then block of code under if statement will be executed if condition is false then block of code under elif statement will be executed if condition is false then block of code under else statement will be executed

"""
 syntax:
 
 if condition:
     
     block of code
     
 elif condition:
     
     block of code
     
 else:
     
     block of code
"""
marks = int(input("Enter your Marks : "))

if ( 90 <=  marks <= 100) :               # if (marks >= 90 and marks <= 100) ) :
    print ("A+")
    
elif (80 <= marks < 90) :                   # elif (marks >= 80 and marks < 90) ) :
    print("B+")
    
elif (marks > 100) :                     # elif (marks < 0 or marks > 100) :
    print("Invalid Marks")
    
else :                                     
    print("C+")
    
    
#OUTPUT
"""
Input : 95
A+

Input : 85
B+

Input : 105
Invalid Marks

Input : 75
C+
""" 