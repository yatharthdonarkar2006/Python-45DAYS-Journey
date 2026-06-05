# break in python

# The break statement is used to exit a loop prematurely when a certain condition is met. It can be used in both for and while loops.

# break is a jumping statement that allows you to exit a loop before it has completed all of its iterations. When the break statement is encountered, the loop is immediately terminated, and the program continues with the next statement after the loop.

# Example of using break in a for loop
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop when i is equal to 5
    print(i)
    
# Output:
# 1
# 2
# 3
# 4
