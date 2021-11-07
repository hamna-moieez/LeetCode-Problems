'''
Given a string s, find the length of the longest substring 
without repeating characters.
'''


s = "dvdf"
s = "abcabcbb"
s = "pwwkew"
s = ""
s = "bbbbb"
# MY SOLUTION - DIRTY
if not s:
    print(0)
substrings = [""]
ind = 0
for i in range(0, len(s)):
    for j in range(i, len(s)):
        if s[j] not in substrings[ind]:
            substrings[ind] += s[j]
        else:
            substrings.append("")
            ind += 1
            break
    print(substrings)
longest_substring = max(substrings, key=len)
print(len(longest_substring))


# GOOD SOLUTION - COPIED
max_l = 0
my_str = ""
for x in s:
    if x not in my_str:
        my_str += x
    else:
        if len(my_str) > max_l:
            max_l = len(my_str)
        my_str = my_str[my_str.find(x)+1:]
        my_str += x
    print(my_str)    
max_l = max(max_l,len(my_str))

print(max_l)
