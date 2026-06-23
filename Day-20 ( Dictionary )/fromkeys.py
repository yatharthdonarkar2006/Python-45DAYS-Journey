# fromkeys() in Dictionary

student = {
    "name": "Yatharth",
    "age": 18
}

d = dict.fromkeys(student, "Non")

print(d)

# Output : {'name': 'Non', 'age': 'Non'}