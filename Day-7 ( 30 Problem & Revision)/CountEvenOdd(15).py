# 16. Count Even and Odd Digits



#Input: 123456
#Even digits = 3
#Odd digits = 3

num = int(input("Enter a number: "))

even_count = 0
odd_count = 0
while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    num = num // 10

print("Even digits = ", even_count)
print("Odd digits = ", odd_count)