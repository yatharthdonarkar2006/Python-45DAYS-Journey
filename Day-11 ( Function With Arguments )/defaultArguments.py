# Default Arguments in Python 

# Default arguments are a powerful feature in Python that allows you to specify default values for function parameters.
# If the caller does not provide a value for a parameter with a default argument, the function will use the default value instead.

# Example of Default Arguments

def my_function(fname, lname=""):
    print(fname + " " + lname)
    
# Calling the function with only the first argument

my_function("Yatharth")
my_function("Yatharth", "Donarkar")

# Output:

# Yatharth Smith
# Yatharth Donarkar