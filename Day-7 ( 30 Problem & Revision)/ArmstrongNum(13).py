# 13. Armstrong Number

# Check whether a number is Armstrong.

num = (int(input("Enter the number : ")))
OriginalNum = num
arm = 0

while num > 0 :
    rem = num % 10
    num = num // 10
    arm = arm + (rem * rem * rem)                         # arm = rem ** 3
    
if (arm == OriginalNum) :
        print ("Armstrong Number is : ", OriginalNum)
    
else : 
        print ("Not an Armstrong Number : ", OriginalNum)
