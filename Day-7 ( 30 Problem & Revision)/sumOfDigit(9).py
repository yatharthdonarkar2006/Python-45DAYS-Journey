# 9. Sum of Digits

#Input: 123
#Output: 6

num = int(input("Enter the Number : "))
sum = 0

while num > 0 :
    digit = num % 10
    sum += digit
    num = num // 10
    
print(sum)