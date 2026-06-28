str1 = "I love python and I love coding"

str = str1.split()
freq = {}

for word in str:
    if(word in freq):
        freq[word]+=1
    else:
        freq[word]=1
        
for keys, values in freq.items():
    print(keys ,":", values )