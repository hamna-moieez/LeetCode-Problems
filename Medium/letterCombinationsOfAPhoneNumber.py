'''
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent. 
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. 
Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

from itertools import product
digits = "273"
mapper = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}

if not digits:
    print("[]")
if len(digits) == 1:
    print(list(mapper[digits[0]]))
combs =[]
lst = []
for i in range(len(digits)):
    val = mapper[digits[i]]
    lst.append(val)
# Find cartesian product of values
for element in product(*lst):
    combs.append(''.join(element))
print(combs)