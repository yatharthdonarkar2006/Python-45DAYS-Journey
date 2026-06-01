# For Loop in Python

#basic syntax of for loop in python

# for variable in sequence:
#     # code block to be executed

for i in range (5):
    print(i)
    
#OUTPUT
    """
    0
    1   
    2
    3
    4
    """
   
for i in range (1, 10, 2):               #range (start, stop, step)
    print(i)
    
    
    #OUTPUT
    """
    1
    3
    5
    7
    9
    """
    
for i in range (10, 0, -1):       
    print(i)
    
    #OUTPUT
    """
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    """
    
    
for i in range (0, 11, 2):           
    print(i)
    
    #OUTPUT
    """
    0
    2
    4
    6
    8
    10
    """