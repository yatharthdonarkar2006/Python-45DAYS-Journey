# 12. Prime Number Check

# Determine whether a number is prime.

num = (int(input("Enter the number : ")))
count = 0

for i in range (2, num) :
    if (num % i == 0) :
        count += 1
        
if(count == 2) :
    print ("Number is Prime", num)
    
else :
    print ("Number is not Prime", num)