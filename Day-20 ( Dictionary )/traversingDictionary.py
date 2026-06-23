# Traversing Dictionary

student = {
    "name": "Yatharth",
    "age": 19
}

# Keys Only

for key in student :                          
    print (key)
    
# Output : 
# name
# age

# Values Only

for value in student.values() :
    print(value)
    
# Output : 
# Yatharth
# 19

# For Both Key & Vaules

for key, value in student.items():
    print(key, value)

# Output : 
# name Yatharth
# age 19