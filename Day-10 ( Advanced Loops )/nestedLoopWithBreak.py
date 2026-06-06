# Nested Loop with break in Python

# In Python, you can use a break statement inside a nested loop to exit the innermost loop. When a break statement is executed, it will only exit the current loop in which it is placed, and the outer loop will continue to execute.

# Example of a nested loop with break:

# Outer loop
for i in range(1, 4):
    print(f"Outer loop iteration: {i}")
    
    # Inner loop
    for j in range(1, 4):
        print(f"  Inner loop iteration: {j}")
        if j == 2:
            print("  Breaking the inner loop at iteration 2")
            break