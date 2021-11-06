'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.
'''

#SLOWER SOLUTION
def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    original_num = x
    reversed_num = 0
    while x != 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10
    if reversed_num == original_num:
        return True
    return False

print(isPalindrome(121))

# FASTER SOLUTION
def isPalindrome(x: int) -> bool:
    if x<0:
        return False
    string_x = str(x)
    reversed_x = string_x[::-1]
    if string_x == reversed_x:
        return True
    return False

print(isPalindrome(-121))