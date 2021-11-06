'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, 
and you may not use the same element twice.
You can return the answer in any order.
'''

from itertools import combinations
nums = [3,4,6]
target =9

#DIRTY SOLUTION
values = list(combinations(nums, 2))
indexes = list(combinations(range(len(nums)), 2))
print(indexes)
print(values)
for count, value in enumerate(values):
    add = sum(value)
    if add == target:
        print(indexes[count])

#WORKING SOLUTION
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
        prev = nums[i]
        curr = nums[j]
        add = prev + curr
        if add == target:
            print([i, j])
            
#BEST SOLUTION
seen = {}
for i, v in enumerate(nums):
    remaining = target - v
    if remaining in seen:
        print([seen[remaining], i])
    seen[v] = i
            
