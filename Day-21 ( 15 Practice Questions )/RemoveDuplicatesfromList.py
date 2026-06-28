ls = [1, 2, 2, 3, 4, 4, 5]

ls_new = []

for i in range(len(ls)):
    if(ls[i] not in ls_new):
        ls_new.append(ls[i])
        
print(ls_new)