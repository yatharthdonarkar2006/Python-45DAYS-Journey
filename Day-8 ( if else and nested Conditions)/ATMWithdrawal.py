"""
Problem 4: ATM Withdrawal
Conditions
Balance ≥ withdrawal amount
Withdrawal amount must be multiple of 100
Minimum balance after withdrawal = 1000
Example
Balance: 10000
Withdraw: 5000

Output:
Balance - Withdraw
Remaining Balance: 5000
    """
    
    
Balance = int(input("Enter your Balance : "))
Withdraw = int(input("Enter your Withdraw Amount : "))

if(Balance >= Withdraw) :
    if(Withdraw % 100 == 0):
        if ((Balance - Withdraw) >= 1000) :
            print( Withdraw , ": Withdraw Successful")
            print("Remaining Balance : ", Balance - Withdraw)
            
        else:
                print("Minimum balance of 1000 must be maintained.")
            
    else:
        print("Withdrawal amount must be a multiple of 100.")
        
else:
    print("Insufficient Balance.")
            
"""
OUTPUT 


Enter your Balance : 5000
Enter your Withdraw Amount : 3000
3000 : Withdraw Successful
Remaining Balance :  2000
    """
            