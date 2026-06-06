# for else in Python 

# The for-else statement in Python is a unique construct that allows you to execute a block of code after a for loop has completed its iterations, but only if the loop was not terminated by a break statement.

# Example of for-else:

for i in range(1, 6):
    print(f"Iteration: {i}")
    if i == 3:
        print("Breaking the loop at iteration 3")
        break
else:
    print("Loop completed without breaking")
    
# In this example, the for loop iterates from 1 to 5. When it reaches iteration 3, it executes the break statement, which terminates the loop. As a result, the else block is not executed because the loop was exited prematurely.

# If we remove the break statement, the else block will be executed after the loop completes all iterations:

for i in range(1, 6):
    print(f"Iteration: {i}")
else:
    print("Loop completed without breaking")
    
# In this case, the for loop iterates from 1 to 5 without any interruption, and after the loop finishes, the else block is executed, printing "Loop completed without breaking".