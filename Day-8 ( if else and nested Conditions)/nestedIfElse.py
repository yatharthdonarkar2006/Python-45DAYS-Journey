# Nested if else statement in python

# A nested if else statement is an if else statement that is placed inside another if else statement.

# syntax of nested if else statement in python

# if condition1:
#     # block of code to be executed if condition1 is true
#     if condition2:
#         # block of code to be executed if condition2 is true
#     else:
#         # block of code to be executed if condition2 is false
# else:
#     # block of code to be executed if condition1 is false

# example of nested if else statement in python

age = 18
if age >= 18:
    print("You are an adult.")
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are a minor.")
    
# in this example, the first condition is age >= 18. If the condition is true, the code block under the first if statement will be executed, and it will print "You are an adult." Then, the second condition is age >= 65. If the second condition is true, the code block under the second if statement will be executed, and it will print "You are a senior citizen."

# If the second condition is false, the code block under the else statement will be executed, and it will print "You are not a senior citizen." If the first condition is false, the code block under the else statement will be executed, and it will print "You are a minor."