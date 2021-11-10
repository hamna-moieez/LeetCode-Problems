
'''
Given a string s, return the longest palindromic substring in s.
'''


# s = "baabaad"
# s ="cbbd"
# s ="ac"
# s = "a"
# s = "fydvdfg"
s = "dvdfgh"
# s = "bb"
# s = "aacabdkacaa"

    


#MY SOLUTION - DIRTY
def longestPalindrome(self, s: str) -> str:
    longest = ""
    if s == s[::-1]:
        return s
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            sub = s[i: j]
            rev = sub[::-1]
            if rev == sub and len(sub) > len(longest):
                    longest = sub
    return(longest)

# SLIGHTLY BETTER SOLUTION
def longestPalindrome(s):
    longest = ""
    if s == s[::-1]:
        return s
    for i in range(len(s)):
        temp = ""
        for j in range(i, len(s)):
            temp += s[j]
            if temp == temp[::-1] and len(temp) > len(longest):
                longest = temp
        print(temp)
    return(longest)
print(longestPalindrome(s))


# MANACHER'S ALGORITHM

def UpdatedString(string):
    newString = ['#']
    for char in string:
        newString += [char, '#']
    return ''.join(newString)

def Manachen(string):
    string = UpdatedString(string)
    LPS = [0 for _ in range(len(string))]
    C = 0
    R = 0

    for i in range(len(string)):
        iMirror = 2*C - i
        if R > i:
            LPS[i] = min(R-i, LPS[iMirror])
        else:
            LPS[i] = 0
        try:
            while string[i + 1 + LPS[i]] == string[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass
        
        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]
    
    r, c = max(LPS), LPS.index(max(LPS))
    print (string[c - r : c + r].replace("#",""))
    return r

print(Manachen(s))



