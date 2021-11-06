
'''
Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages,
you must instead have the result be placed in the first part of the array nums.
More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. 
It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. 
You must do this by modifying the input array in-place with O(1) extra memory.
'''

nums = [0,0,1,1,1,2,2,3,3,4]

# NORMAL SOLUTION
curr = 0
runner = 1
for i in nums:
    try:
        if nums[curr] == nums[runner]:
            nums[curr] = None
        curr += 1
        runner += 1
    except:
        pass
nums = [x for x in nums if x is not None]
print(nums)
print(len(nums))

# INPLACE SOLUTION - DIRTY/FASTER
curr = 0
runner = 1
for i in nums:
    try:
        if nums[curr] == nums[runner]:
            nums[curr] = None

        curr += 1
        runner += 1
    except:
        pass
try:
    while True:
        nums.remove(None)
except ValueError:
    pass

print(nums)
print(len(nums))


# INPLACE SOLUTION - CLEANER/SLOWER
curr = 0
runner = 1
if not nums:
    print(0)
for i in nums:
    try:
        if nums[curr] == nums[runner]:
            nums[curr] = None
            nums.append(nums.pop(nums.index(None)))
        else:
            curr += 1
            runner += 1
    except:
        pass
k = len(nums) - nums.count(None)
print(k)
print(nums)

#DOUBLE LOOP
for i in range(len(nums)):
    for j in range(len(nums)-1, 0, -1):
        if nums[i] == nums[j] and i!=j:
            nums[i] = None
            break
try:
    while True:
        nums.remove(None)
except ValueError:
    pass
print(nums)

#SIMPLEST SOLUTION
curr, runner = 0, 1
n = len(nums)-1
while n>0:
    if nums[curr] == nums[runner]:
        del nums[curr]
    else:
        curr += 1
        runner += 1
    n -=1
print(nums)


