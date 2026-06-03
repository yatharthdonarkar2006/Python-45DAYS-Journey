# 14. Palindrome Number

# Check if a number reads same from both sides.

# Example:

# 121 → Palindrome


num = (int(input("Enter the number : ")))
OriginalNum = num
rev = 0

while num > 0:
    digit = num % 10
    rev = rev + digit * 10
    num = num // 10

if rev == OriginalNum:
    print("Palindrome Number is : ", OriginalNum)
else:
    print("Not a Palindrome Number : ", OriginalNum)