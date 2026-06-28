ls = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for i in range(len(ls)):
    if(ls[i] % 2 == 0):
        even +=1
    else:
        odd +=1
        
print("Even : ", even )
print("Odd : ", odd)