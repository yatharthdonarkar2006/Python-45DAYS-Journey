# Sum of Digits


def sum(nums):
    total = 0
    while nums > 0:
        lastDigit = nums % 10
        total += lastDigit
        nums = nums // 10
        
        
    return total 

nums = (int(input("Enter the Number : ")))
total = (sum(nums))
print(total)
