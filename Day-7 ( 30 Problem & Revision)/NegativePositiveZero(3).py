# 3. Positive, Negative, or Zero

# Take a number and determine its type.

num = (int(input(" Enter The Number : ")))

if(num == 0):
    print("Number is Zero", num)
    
elif(num > 0) :
    print ("Number is Positive", num)

else :
    print ("Number is Negative", num)
    
# OUTPUT 

    """
    Enter The Number : 4
    Number is Positive 4
    
    Enter The Number : -9
    Number is Negative -9
    
    Enter The Number : 0
    Number is Zero 0
    
    """