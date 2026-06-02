# Keyword Arguments Function in Python

# Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name. This allows you to skip arguments or place them in a different order because the Python interpreter is able to use the keywords provided to match the values with parameters.

# Creating a Function with Keyword Arguments

def my_function(child3, child2, child1):
    print("The youngest child is " + child3)     # In this function, we have defined three parameters: child3, child2, and child1. When we call the function, we can use keyword arguments to specify which value corresponds to which parameter. For example, we can call the function with my_function(child1="Emil", child2="Tobias", child3="Linus"). This way, we are explicitly stating that "Emil" is the value for child1, "Tobias" is the value for child2, and "Linus" is the value for child3. The function will then print "The youngest child is Linus" because we have assigned "Linus" to the parameter child3.
    
# Calling a Function with Keyword Arguments
my_function(child1="Emil", child2="Tobias", child3="Linus")         # When we call the function with keyword arguments, we can specify the values for each parameter in any order. In this case, we are assigning "Emil" to child1, "Tobias" to child2, and "Linus" to child3. The function will then print "The youngest child is Linus" because we have assigned "Linus" to the parameter child3. This demonstrates how keyword arguments allow us to call a function with arguments in a different order than they are defined in the function.

# Output: The youngest child is Linus

# You can also use keyword arguments when you call a function with default parameter values.
# This way, you can change the default values if needed.

def my_function2(child1="Emil", child2="Tobias", child3="Linus"):
    print("The youngest child is " + child3)     # In this function, we have defined three parameters with default values: child1 is "Emil", child2 is "Tobias", and child3 is "Linus". When we call the function without providing any arguments, it will use these default values. However, if we want to change the default value for child3, we can use a keyword argument when calling the function. For example, if we call my_function(child3="Anna"), it will override the default value of child3 and print "The youngest child is Anna". This allows us to easily modify the behavior of the function without changing its definition.
    
my_function2(child3="Anna")         # When we call the function with the keyword argument child3="Anna", it will override the default value of child3, which is "Linus". Therefore, the function will print "The youngest child is Anna". This demonstrates how we can use keyword arguments to change the default values of parameters when calling a function.

# Output: The youngest child is Anna