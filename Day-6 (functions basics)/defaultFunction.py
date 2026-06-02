# Default Function in Python

# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. 
# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Creating a Function with Default Parameter
def my_function(*kids):
    print("The youngest child is " + kids[2])     # The *kids parameter allows the function to accept an arbitrary number of arguments. In this case, we can pass multiple names as arguments when calling the function. The function will receive these names as a tuple, and we can access them using indexing. For example, kids[2] will give us the third name in the tuple, which is "Tobias" in this case.
    
# Calling a Function with Default Parameter
my_function("Emil", "Tobias", "Linus")         # When we call the function with the arguments "Emil", "Tobias", and "Linus", it will print "The youngest child is Tobias". This is because we passed three names as arguments, and the function accesses the third name (index 2) to determine the youngest child.

# Example 2

def add(a=10, b=20):           # In this example, we have defined a function called add that takes two parameters, a and b. We have assigned default values of 10 and 20 to these parameters, respectively.#        This means that if we call the function without providing any arguments, it will use these default values.
    print(a+b)            # The function will print the sum of a and b. If we call the function without any arguments, it will add the default values (10 + 20) and print 30. However, if we provide our own values for a and b when calling the function, it will use those values instead of the defaults.
    
add()                   # When we call the function without any arguments, it will use the default values of a and b, which are 10 and 20. Therefore, it will print 30.