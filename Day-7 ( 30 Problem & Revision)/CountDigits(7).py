# 7. Count Digits

# Input a number and count how many digits it contains.

# Example:

# Input: 12345
# Output: 5


    
num = int(input("Enter a number: "))

count = 0

while num > 0:
    num = num // 10
    count += 1

print("Number of digits =", count)

