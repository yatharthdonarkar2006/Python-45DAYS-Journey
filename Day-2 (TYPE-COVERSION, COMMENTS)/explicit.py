# Explicit Type Conversion (Type Casting)

# In explicit type conversion, the programmer manually converts one data type to another using built-in functions. This is often necessary when you want to ensure that a specific data type is used for an operation.
# Example of explicit type conversion
# also known as type casting

# Converting a string to an integer
num_str = "123"
num_int = int(num_str)               # Using the int() function to convert the string to an integer
print(num_int)  # Output: 123

# Converting a float to an integer
num_float = 4.55;
num_int = int(num_float)             # Using the int() function to convert the float to an integer (truncates the decimal part)
print(num_int)  # Output: 4          # Note: This does not round the number, it simply truncates the decimal part.

# Converting an integer to a float
num_int = 10
num_float = float(num_int)           # Using the float() function to convert the integer to a float
print(num_float)  # Output: 10.0

# Converting a string to a float
num_str = "3.14"
num_float = float(num_str)           # Using the float() function to convert the string to a float
print(num_float)  # Output: 3.14

# Converting a string to a boolean
bool_str = "true"
bool_value = bool(bool_str)          # Using the bool() function to convert the string to a boolean
print(bool_value)  # Output: True   # Note: In Python, any non-empty string is considered True when converted to a boolean, while an empty string is considered False.

# Converting a boolean to an integer
bool_value = True
num_int = int(bool_value)           # Using the int() function to convert the boolean to an integer
print(num_int)  # Output: 1        # Note: In Python, True is converted to 1 and False is converted to 0 when using the int() function.

# Converting a boolean to a float
bool_value = False
num_float = float(bool_value)       # Using the float() function to convert the boolean to a float
print(num_float)  # Output: 0.0     # Note: In Python, False is converted to 0.0 when using the float() function.

