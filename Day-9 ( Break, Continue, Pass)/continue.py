# continue in Python

# The continue statement is used to skip the current block of code and move to the next iteration of the loop.

# continue is a jumping statement that allows you to skip the rest of the code inside a loop for the current iteration and move on to the next iteration. When the continue statement is encountered, the loop does not terminate but instead skips the remaining code and proceeds with the next iteration.

# Example of using continue in a for loop
for i in range(1, 11):
    if i == 5:
        continue  # Skip the rest of the code when i is equal to 5
    print(i)
    
# Output:

# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10
