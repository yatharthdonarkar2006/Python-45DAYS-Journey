# Largest Among Three Numbers

def largest(num1, num2, num3):
    
        
    if(num1 > num2 and num1 > num3):
        return num1
    elif(num2 > num1 and num2 > num3):
        return num2
    else:
        return num3

num1 = (int(input("Enter the Number : ")))
num2 = (int(input("Enter the Number : ")))
num3 = (int(input("Enter the Number : ")))

print(largest(num1, num2, num3))
