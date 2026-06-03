# 11. Factorial Using Loop
# Find factorial of a number.
# Example:
# 5! = 120

num = (int(input("Enter the number : ")))
fact = 1

for i in range (1, num + 1) :
    fact *= i
    
    
print(fact)
    
    # output 
"""Enter the number : 5
120 
"""
    