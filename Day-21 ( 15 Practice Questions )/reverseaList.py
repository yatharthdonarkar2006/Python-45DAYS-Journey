ls = [1, 2, 3, 4, 5]

reverse = ls[ ::-1]    #1st Option

ls.reverse()           #2nd Option

print(reverse)
print(ls)
    
    
for i in range(len(ls)-1,-1,-1):
    print([i])