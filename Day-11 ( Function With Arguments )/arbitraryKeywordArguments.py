# Arbitrary Keyword Arguments (**kwargs) in Python

# Arbitrary Keyword Arguments (**kwargs) is used when the number keyword arguments is Unknown.

def my_Fun(**nums):
 print(nums)

my_Fun(fname="Yatharth", lname ="Donarkar", age=20)

# Output : {'fname': 'Yatharth', 'lname': 'Donarkar', 'age': 20}