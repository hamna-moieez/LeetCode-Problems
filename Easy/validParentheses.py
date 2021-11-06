'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

'''


def isValid(s):
    valid = {'(':')', "{":"}", "[":"]"}
    stack = []
    
    if not s:
        return False
    for character in s:
        if character in valid.keys():
            stack.append(character)
        else:
            try:
                key = stack[-1]
                if key in valid and valid.get(key) == character:
                    stack.pop()
                else:
                    return False
            except:
                return False

    if not stack:
        return True
    else:
        return False
        

s = "(])"
print(isValid(s))