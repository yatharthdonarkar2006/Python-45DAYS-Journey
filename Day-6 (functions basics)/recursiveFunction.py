# Recursion in Python

# Recursion is a programming technique where a function calls itself in order to solve a problem. A recursive function typically has a base case that stops the recursion and a recursive case that breaks the problem into smaller subproblems.

# Creating a Recursive Function

def MyFun(n):
    if n <=1:
        return 1
    
    return MyFun(n - 1)
                      # When we call the function MyFun with the argument 5, it will calculate the sum of all numbers from 1 to 5. The function will call itself with n - 1 until it reaches the base case where n is 0. The result will be 15, which is the sum of 1 + 2 + 3 + 4 + 5.  

print(MyFun(int(input("Enter a number: "))))      

# Output: Enter a number: 5
#         15