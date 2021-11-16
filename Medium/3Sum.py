'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
'''

from itertools import combinations

# nums = [-1,0,1,2,-1,-4]
nums = [0,0,0]
# nums = [-1,0,1,0]

#WORKING SOLUTION
nums.sort()
out=[]
for i in range(len(nums)):
    if i > 0 and nums[i]== nums[i - 1]: 
        continue  
    left = i+1
    right = len(nums)-1
    while left < right:
        add = nums[i] + nums[left] + nums[right]
        if add < 0:
            left += 1
        elif add > 0:
            right -= 1
        else:
            out.append([nums[i], nums[left], nums[right]])
            left += 1
            right -= 1
            while nums[left] == nums[left - 1] and left < right:
                left += 1

print(out)

#-------TIME LIMIT EXCEEDED SOLUTIONS----------

# nums.sort()
# out = []
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         if i != j:
#             diff = nums[i] + nums[j]
#             target = -(diff)
#             if target in nums and (nums.index(target) != i and nums.index(target) != j):
#                 triplet = [nums[i], nums[j], target]
#                 triplet.sort()
#                 if triplet not in out:
#                     out.append(triplet)
# print(out)



# nums.sort()
# out = []
# nums.sort()
# combination = combinations(nums, 3)
# for i in list(combination):
#     if sum(i) == 0 and i not in out :
#         out.append(i)
# print(out)



# out = []
# nums.sort()
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         for k in range(j+1, len(nums)):
#             lst = [nums[i], nums[j], nums[k]]
#             if nums[i] + nums[j] + nums[k] == 0 and lst not in out:
#                 out.append(lst)
# print(out)



# out = []
# if not nums or len(nums) < 3:
#     print ([])
# if nums.count(0) >=3:
#     out.append([0,0,0])
# pos = [x for x in nums if x>=0]
# neg = [x for x in nums if x<=0]
# mp_pos = {}
# mp_neg = {}
# for x in range(len(pos)):
#     for y in range(x + 1, len(pos)):
#         mp_pos[tuple([pos[x], pos[y]])] = pos[x] + pos[y]
# for x in range(len(neg)):
#     for y in range(x + 1, len(neg)):
#         mp_neg[tuple([neg[x], neg[y]])] = neg[x] + neg[y]
# s = sorted(set(nums))
# triplet = []

# for i in s:
#     if i < 0:
#         for key, value in mp_pos.items():
#             if abs(i) == value:
#                 triplet = [i] + list(key)
#                 triplet.sort()
#                 if triplet not in out:
#                     out.append(triplet)
#     if i > 0:
#         for key, value in mp_neg.items():
#             if i == abs(value):
#                 triplet = list(key) + [i]
#                 triplet.sort()
#                 if triplet not in out:
#                     out.append(triplet)
        
# print(out)

    
