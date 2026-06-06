# Looping Through Collections in Python

# In Python, you can loop through various types of collections such as lists, tuples, dictionaries, and sets using different types of loops. Here are some examples of how to loop through these collections:

# Looping through a list
my_list = [1, 2, 3, 4, 5]
print("Looping through a list:")

for item in my_list:
    print(item)

# Looping through a tuple
my_tuple = (6, 7, 8, 9, 10)
print("\nLooping through a tuple:")
for item in my_tuple:
    print(item)

# Looping through a dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
print("\nLooping through a dictionary:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Looping through a set
my_set = {11, 12, 13, 14, 15}
print("\nLooping through a set:")
for item in my_set:
    print(item)