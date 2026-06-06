# Nested Loop in Python

# Nested loops are loops that are placed inside another loop. The inner loop will be executed one time for each iteration of the outer loop.

# Example of a nested loop:

# Outer loop
for i in range(1, 4):
    print(f"Outer loop iteration: {i}")
    
    # Inner loop
    for j in range(1, 4):
        print(f"  Inner loop iteration: {j}")
        
# In this example, the outer loop runs 3 times (i = 1, 2, 3), and for each iteration of the outer loop, the inner loop also runs 3 times (j = 1, 2, 3). This results in a total of 9 iterations of the inner loop (3 iterations of the outer loop * 3 iterations of the inner loop).
# Output:
# Outer loop iteration: 1
#   Inner loop iteration: 1
#   Inner loop iteration: 2
#   Inner loop iteration: 3
# Outer loop iteration: 2
#   Inner loop iteration: 1
#   Inner loop iteration: 2
#   Inner loop iteration: 3
# Outer loop iteration: 3
#   Inner loop iteration: 1
#   Inner loop iteration: 2
#   Inner loop iteration: 3