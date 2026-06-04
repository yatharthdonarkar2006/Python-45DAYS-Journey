# Problem 5: Admission Eligibility 
"""
Conditions

A student gets admission if:

Maths ≥ 70
Physics ≥ 60
Chemistry ≥ 60

AND

Total of all subjects ≥ 200

OR

Maths + Physics ≥ 150
"""

Maths_Marks = int(input("Enter your Marks of Maths : "))
Physics_Marks = int(input("Enter your Marks of Physics : "))
Chemistry_Marks = int(input("Enter your Marks of Chemistry : "))

if (Maths_Marks >=70 and Physics_Marks >= 60 and Chemistry_Marks >= 60)  :
    print ("You will Get Addmission 1 ")
    
    if((Maths_Marks + Physics_Marks + Chemistry_Marks) >= 200 ) or ((Maths_Marks + Physics_Marks) >= 150):
    print ("You will Addmission 2")
    
    else :
    print (" Not ")
    
else :
    print (" Not ")