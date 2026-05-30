# Keywords in Python

# Keywords are reserved words in Python that have a specific meaning and cannot be used as identifiers (variable names, function names, etc.). They are used to define the syntax and structure of the Python language.

# Here is a list of some common keywords in Python:
""""
# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert      del        global     not        with
# async       elif       if         or         yield
"""
# As of Python 3.10, there are 35 keywords in total. You can get the list of keywords in your Python environment using the following code:
import keyword
print(keyword.kwlist)
# Output will be a list of all the keywords in Python.
# It's important to note that keywords are case-sensitive, meaning that "if" is a keyword, but "If" or "IF" would not be recognized as a keyword and could be used as an identifier.
# Example of using keywords:
def my_function():
    if True:
        return "This is a keyword example."
    else:
        return "This will never be executed."       
print(my_function())
# In this example, "def", "if", "True", "return", and "else" are all keywords used to define the function and control the flow of the program.
# Remember that you cannot use keywords as variable names or function names. For example, the following code will result in a syntax error:
# def if():
#     pass
# In this case, "if" is a keyword and cannot be used as a function name. Always choose identifiers that are not keywords to avoid syntax errors in your code.

# self is commonly used in classes, but it is not a Python keyword.