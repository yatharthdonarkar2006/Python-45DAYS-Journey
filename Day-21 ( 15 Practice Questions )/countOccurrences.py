# Count Occurrences

tp = (1, 2, 2, 3, 2, 4)
n = int(input("Enter the no. "))
count = 0
for num in tp :
    if(num == n):
        count+=1
        
print(count)