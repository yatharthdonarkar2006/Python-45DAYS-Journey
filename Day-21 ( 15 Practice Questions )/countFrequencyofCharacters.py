str = input("Enter the String : ")

freq = {}

for ch in str:
    if(ch in freq):
        freq[ch]+=1
    else:
        freq[ch]=1
        
# for key, value in freq.items(): 
#     print(key, ":", value)
print(freq)