# Number Guessing Game

key = 25

while True:
    n = (int(input("Enter the Key : ")))
    
    if (n == key):
        print("You Won ")
        break
    
    elif (n > key) :
        print("Too High")
        
    else :
        print("Too Low")
    
    

