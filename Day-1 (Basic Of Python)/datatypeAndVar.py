#there are 8 Data Types in Python (Basic Data Types and their more complex data types)


name ="Yatharth Donarkar"       #String Data Type
age = 20                        #Integer Data Type
height = 5.8                    #Float Data Type
city = "Nagpur"                 #String Data Type
is_student = True               #Boolean Data Type  
list_of_numbers = [1, 2, 3, 4, 5]   #List Data Type  (Store multiple collection of similar or different data types and it is a ordered collection of data and it is mutable)
tuple_of_numbers = (1, 2, 2, 1, 4, 5)   #Tuple Data Type (Store multiple collection of similar or different data types and it is a ordered collection of data and it is immutable)
set_of_numbers = {1, 2, 3, 4, 5}    #Set Data Type    (Store multiple collection of similar or different data types and it is a unordered collection of data and it is mutable and it does not allow duplicate values)
dictionary_of_person = {"name": "Yatharth Donarkar", "age": 20, "height": 5.8, "city": "Nagpur", "is_student": True}   #Dictionary Data Type (Store multiple collection of similar or different data types and it is a unordered collection of data and it is mutable and it stores data in key-value pairs)


print("My Name is",name ,"and I am",age,"years old. I am",height,"feet tall and I live in",city,". It is",is_student,"that I am a student.")
print(list_of_numbers)
print(tuple_of_numbers)
print(dictionary_of_person)
print(set_of_numbers)

# Output : My Name is Yatharth Donarkar and I am 20 years old. I am 5.8 feet tall and I live in Nagpur . It is True that I am a student.
# [1, 2, 3, 4, 5]
# (1, 2, 2, 1, 4, 5)    
# {'name': 'Yatharth Donarkar', 'age': 20, 'height': 5.8, 'city': 'Nagpur', 'is_student': True}
# {1, 2, 3, 4, 5}