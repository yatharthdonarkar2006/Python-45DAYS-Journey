# Removing Elements 

# pop() : remove the element 

dict = {"Name":"Yatharth" , "Roll-no":52, "City":"Mansar", "class":"2nd Year"}

dict.pop("Name")
print(dict)

# Output : {'Roll-no': 52, 'City': 'Mansar', 'class': '2nd Year'}

# popitem : remove the last inserted item

dict["A"] = "B"
print(dict)

# Output : {'Roll-no': 52, 'City': 'Mansar', 'class': '2nd Year', 'A': 'B'}

dict.popitem()  # Remove the last inserted Element 
print(dict)

# Output : {'Roll-no': 52, 'City': 'Mansar', 'class': '2nd Year'}


# del

del dict["class"]
print(dict)

# Output : {'Roll-no': 52, 'City': 'Mansar'}