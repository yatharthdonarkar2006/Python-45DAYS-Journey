# Problem 2: Perfect Number
# A number is perfect if the sum of its proper divisors equals the number.

num = (int(input("Enter the number : ")))
OriginalNum = num
sum = 0


for i in range (1, num):
    if(num % i == 0):
        print (i)
        sum += i
        if(sum == OriginalNum) :
            print (f"Done {sum}")
        
    