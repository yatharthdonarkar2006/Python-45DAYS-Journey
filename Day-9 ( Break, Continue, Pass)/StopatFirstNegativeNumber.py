# Stop at First Negative Number

nums = [10, 20, 30, -5, 40, 50]

for i in range (0, 6) :
    if (nums[i] < 0) :
        break
    print (nums[i])
    
# Output
"""
10
20
30
"""