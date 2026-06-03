# 2. Largest of Three Numbers

# Input three numbers and print the largest.

num1 = (int(input("enter the num1 : ")))
num2 = (int(input("enter the num2 : ")))
num3 = (int(input("enter the num3 : ")))

if (num1 > num2 and num1 > num3) :
    print(num1 , "is Largest")
    
elif (num2 > num1 and num2 > num3) :
    print(num2 , "is Largest")
    
else :
    print(num3 , "is Largest")

# OUTPUT 
"""
enter the num1 : 3
enter the num2 : 4
enter the num3 : 5
5 is Largest
"""