# Sorting list

nums = [20, 10, 90, 100, 50, 2, 53, 9]

print(nums)

print (sorted(nums))     # num.sort()   also used

# Output : 
# [20, 10, 90, 100, 50, 2, 53, 9]     //  before sorting
# [2, 9, 10, 20, 50, 53, 90, 100]     // after sorting


# reverse sorting

nums.sort(reverse = True)
print(nums)

# output : [100, 90, 53, 50, 20, 10, 9, 2]