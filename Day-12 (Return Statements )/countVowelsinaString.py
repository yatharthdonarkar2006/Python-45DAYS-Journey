# Count Vowels in a String

def vowels(word):
    count = 0
    for ch in word :
        
        if(ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u" ) :
            count += 1

    return count

word = (input("Enter the String : ")).lower()
result = vowels(word)
print(result)



