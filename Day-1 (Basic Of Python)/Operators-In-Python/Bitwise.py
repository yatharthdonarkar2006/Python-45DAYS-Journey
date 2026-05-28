# Bitwise Operators In Python

"""
Bitwise Operators Works in the Binary 0's and 1's)
"""

# Bitwise operators are used to perform bitwise operations on integers.

# The following are the bitwise operators in Python:

# & (AND)
# | (OR)
# ^ (XOR)
# ~ (NOT)
# << (Left Shift)
# >> (Right Shift)

a = 10  # In Binary 1010
b = 5  # In Binary 0101 

print(a & b)  # Output will be 0 (In Binary 0000)

# a   b    a&b
# 1   0     0
# 0   1     0
# 1   0     0
# 0   1     0

print(a | b)  # Output will be 15 (In Binary 1111)

# a   b    a|b
# 1   0     1
# 0   1     1
# 1   0     1
# 0   1     1
 
print(a ^ b)  # Output will be 15 (In Binary 1111)

# a   b    a^b
# 1   0     1
# 0   1     1
# 1   0     1
# 0   1     1

print(~a)  # Output will be -11 (In Binary 0101)

# a   ~a
# 1   0
# 0   1
# 1   0
# 0   1

print(~b)  # Output will be -6 (In Binary 1010)

# a   ~b
# 0   1
# 1   0
# 0   1
# 1   0

print(a << 2)  # Output will be 40 (In Binary 101000)

# 1010 << 2 = 101000 (In Binary) shift left by 2 bits

print(a >> 2)  # Output will be 2 (In Binary 10)

# 1010 >> 2 = 0010 (In Binary) shift right by 2 bits

