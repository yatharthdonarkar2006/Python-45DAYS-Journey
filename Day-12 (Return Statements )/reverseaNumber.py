# Reverse a Number

def reverse(nums):
    rev = 0
    while nums > 0:
        lastDigit = nums % 10
        rev = rev * 10 + lastDigit
        nums = nums // 10
        
        
    return rev 

nums = (int(input("Enter the Number : ")))
rev = (reverse(nums))
print(rev)
