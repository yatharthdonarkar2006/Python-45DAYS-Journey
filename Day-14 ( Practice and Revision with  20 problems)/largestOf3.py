num1 = int(input("Enter the Num1 : "))
num2 = int(input("Enter the Num2 : "))
num3 = int(input("Enter the Num3 : "))

if(num1 > num2 and num1 > num3):
    print(num1, " Is Largest")
    
elif(num2 > num1 and num2 > num3):
    print(num2, " Is Largest")
    
else:
    print(num3, " Is Largest")