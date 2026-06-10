num = int(input("Enter the Number : "))
OriginalNum = num
rev= 0
while num > 0 :
    lastdigit = num % 10
    rev = rev*10 + lastdigit
    num = num //10
    
if(OriginalNum == rev):
    print(f"{rev}  It is a Palindrome")
    
else:
    print(f"{rev}  It is not a Palindrome")
    
