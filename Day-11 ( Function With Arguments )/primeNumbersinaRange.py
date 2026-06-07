# Problem 2: Prime Numbers in a Range
# Create a function that takes two arguments (start and end) and prints all prime numbers between them.

def prime(start, end):
    
    for num in range (start, end+1) :
        count = 0
        
        for i in range (1, num+1) :
            if(num % i == 0):
                count +=1
                
        if (count == 2):
                print(num)
                
start = (int(input("Enter the Starting point :")))
end = (int(input("Enter the Ending point :")))

prime(start, end)