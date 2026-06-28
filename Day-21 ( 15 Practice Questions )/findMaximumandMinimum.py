tp = (10, 45, 23, 89, 12)

max = 0
min = 0

for i in range (len(tp)) :
    for j in range (len(tp)): 
        if(tp[i] > tp[j]):
            max = tp[i]
            min = tp[j]
        elif(tp[i] < tp[j]):
            max = tp[j]
            min = tp[i]
            
print(max, min)