"""
Problem 3: Employee Bonus System
Rules
Experience ≥ 10 years
Salary > 50000 → Bonus = 20%
Salary ≤ 50000 → Bonus = 15%
Experience < 10 years
Salary > 50000 → Bonus = 10%
Salary ≤ 50000 → Bonus = 5%
"""

experience = (int(input("Enter your Experience : ")))
salary = (int(input("Enter your Salary : ")))

if (experience >= 10):
    if(salary > 50000):
        print("20% Bonus")
        
    elif (salary <= 50000):
        print("15% Bonus")
        
    else :
        print ("Invalid Input")

elif ( experience < 10 ) :
    if(salary > 50000):
        print("10% Bonus")
        
    elif (salary <= 50000):
        print("5% Bonus")
        
    else :
        print ("Invalid Input")
        
else :
        print ("Invalid Input")