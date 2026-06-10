num = int(input("Enter the Number : "))
rev= 0
count = 0
while num > 0 :
    lastdigit = num % 10
    rev = rev*10 + lastdigit
    num = num //10
    count+=1
    
print(rev)
print(count)