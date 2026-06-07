# Problem 4: Frequency of Each Character
# Create a function that takes a string as an argument and prints the frequency of each character.

def char_frequency(text):
    
    freq = {}

    for ch in text:

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    for key, value in freq.items():
        print(key, ":", value)

text = (input("Enter the string : "))
char_frequency(text)
        