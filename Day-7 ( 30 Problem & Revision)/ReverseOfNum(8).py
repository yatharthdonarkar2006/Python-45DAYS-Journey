# 8. Reverse a Number

# Input: 1234
# Output: 4321

num =(int(input("Enter the Number : ")))
reverse = 0

while (num > 0) :
    digit = num % 10 
    reverse = reverse * 10 + digit 
    num = num // 10 
    
print ("The Reverse Number is : " , reverse)