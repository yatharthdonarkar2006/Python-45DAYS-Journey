# Passing Function as Argument in python
"""
In Python, functions are first-class objects, which means you can:

Store them in variables
Pass them as arguments to other functions
Return them from functions
"""
# Syntax
"""
def function1():
    # code

def function2(func):
    func()

function2(function1)
"""

def greet():
    print("Hello from greet") 
    
def my_function(my_fun):
    my_fun()
    
my_function(greet)

# Output : Hello from greet