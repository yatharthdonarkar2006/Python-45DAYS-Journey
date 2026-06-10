def gcd(num1, num2):
    gcd1 = 1
    for i in range (1 , min(num1, num2)+1):
        if(num1 % i == 0 and num2 % i == 0 ):
            gcd1 = i
            
    print(gcd1) 
    

num1 = int(input("Enter the num1 : "))
num2 = int(input("Enter the num2 : "))
gcd(num1, num2)


