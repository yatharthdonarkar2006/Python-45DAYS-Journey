# Using get function return 'none' if key not found

dict = {"Name":"Yatharth" , "Roll-no":52, "City":"Mansar", "class":"2nd Year"}

print(dict.get("key"))
# output : None

print(dict["key"])
# output : KeyError: 'key'
