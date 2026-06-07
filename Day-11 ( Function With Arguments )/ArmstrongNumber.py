# Problem 1: Armstrong Number Function
# Create a function that takes a number as an argument and checks whether it is an Armstrong number.

def arm(num) :
    sum = 0
    a = num
    while a > 0 :
        last_digit = a % 10
        sum += last_digit ** 3
        a = a // 10
        
    if( num == sum) :
        print("ArmStrong")
    
    else :
        print("Not ArmStrong")

        

        
num = (int(input("Enter the Number : ")))
arm(num)

