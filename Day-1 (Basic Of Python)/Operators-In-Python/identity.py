#identity Operators in Python
# Identity Operators are used to Compare the Memory Location of Two Objects.
"""
( is )        operator returns True if both variables (operands) refer to the same object in memory, otherwise it returns False.
( is not )    operator returns True if both variables (operands) do not refer to the same object in memory, otherwise it returns False.
""" 
a = 10
b = 10

print (a is b)  # Output will be True
print (a is not b)  # Output will be False
