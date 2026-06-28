name = {
        "Rahul": 80,
        "Aman": 95,
        "Priya": 88
}

max = 0


for names, marks in name.items():
    
    if(marks > max):
        max=marks
        
print(max)