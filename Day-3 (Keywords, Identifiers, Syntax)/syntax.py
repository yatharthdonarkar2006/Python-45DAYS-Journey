# Basic Syntax of Python

# The basic syntax of Python is designed to be easy to read and write. Here are some key points about Python's syntax:

# 1. Indentation: Python uses indentation to define blocks of code. This means that the level of indentation (usually 4 spaces) indicates which statements belong to which blocks. For example:
if True:
    print("This is a block of code.")
    print("It is indented to indicate that it belongs to the if statement.")
    
# 2. Comments: You can use the hash symbol (#) to add comments to your code. Comments are ignored by the Python interpreter and are used to explain the code or make notes for yourself or other developers.
# This is a single-line comment.
""" multi-line comments can be created using triple quotes. """

# 3. Variables: You can create variables in Python by simply assigning a value to a name. Python is dynamically typed, so you don't need to declare the type of the variable.
x = 10  # This is a variable assignment.
name = "Yatharth"  # This is another variable assignment.

# 4. Functions: You can define functions in Python using the def keyword. Functions are reusable blocks of code that perform a specific task.
def greet(name):
    return f"Hello, {name}!"
print(greet("Yatharth"))  # This will call the greet function and print the result.
#output: Hello, Yatharth!

# 5. Control Flow: Python provides various control flow statements such as if, for, while, and try-except to control the flow of your program.

# Example of an if statement:
age = 20
if age >= 18:
    print("You are an adult.")
    
# Example of a for loop:
for i in range(5):
    print(i)

# Example of a while loop:
count = 0
while count < 5:
    print(count)
    count += 1
    
# Example of a try-except block:
try:
    result = 10 / 0  # This will raise a ZeroDivisionError.
except ZeroDivisionError:
    print("You cannot divide by zero.")
    
# These are just some of the basic syntax elements of Python. As you continue to learn and practice, you'll become more familiar with the various features and capabilities of the language.

