# while else statement in Python

# The while-else statement in Python is similar to the for-else statement. 

# It allows you to execute a block of code after a while loop has completed its iterations, but only if the loop was not terminated by a break statement.

# Example of while-else:

count = 0
while count < 5:
    print(f"Count: {count}")
    if count == 3:
        print("Breaking the loop at count 3")
        break
    count += 1
else:
    print("Loop completed without breaking")

# In this example, the while loop iterates as long as count is less than 5. When count reaches 3, it executes the break statement, which terminates the loop. As a result, the else block is not executed because the loop was exited prematurely.