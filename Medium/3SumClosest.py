'''
Given an integer array nums of length n and an integer target, 
find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''


from itertools import  combinations
# nums = [-1,2,1,-4]
# nums = [1,1,-1,-1,3]
nums = [1,1,48,50,99,100,103,333,333]
target = 250

#WORKING SOLUTION

def threeSumClosest(nums, target):
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    if closest == target:
        return closest
    ini = abs(closest - target)
    for i in range(len(nums)):
        if i > 0 and nums[i]== nums[i - 1]: 
            continue
        if closest == target:
            break  
        left = i+1
        right = len(nums)-1
        while left < right:
            add = nums[i] + nums[left] + nums[right]
            diff = abs(add - target)
            if add < target:
                left += 1
                if diff < ini:
                    ini = diff
                    closest = add
            elif add > target:
                right -= 1
                if diff < ini:
                    ini = diff
                    closest = add
            else:
                closest = target
                break
    return closest
        
print(threeSumClosest(nums, target))



#-------TIME LIMIT EXCEEDED SOLUTIONS----------

# combination = combinations(nums, 3)
# combs = list(combination)
# add = sum(combs[0])
# ini = abs(add - target)
# for i in combs:
#     distance = abs(sum(i) - target)
#     if distance < ini:
#         ini = distance
#         add = sum(i)
# print(add)

