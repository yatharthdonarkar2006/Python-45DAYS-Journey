# Problem 3: Second Largest Element
# Create a function that takes a list as an argument and returns the second largest element.

def my_fun(nums) :
    
    largest = nums[0]
    second = nums[0]
    
    for num in nums :
        
        if (num > largest ):
            second = largest
            largest = num
            
        elif(num > second and num != largest ):
            second = num 
            
    print(second)

nums = list(map(int, input("Enter the List : ").split()))

my_fun(nums)


            