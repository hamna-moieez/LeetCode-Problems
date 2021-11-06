import random

def longestCommonPrefix(strs):
    out = ""
    if len(strs) == 1:
        return strs[0]
    elif len(strs) > 1:
        random_list = random.choices(strs, k=3)
        char1 = random_list[0][:1]
        char2 = random_list[1][:1]
        char3 = random_list[2][:1]
        if char1 != char2 != char3:
            return out
        else:
            shortest = min(strs, key=len)
            for c, val in enumerate(shortest):
                for i in range(len(strs)):
                    if val != strs[i][c]:
                        return out

                out += val
            return out

strs = ["flower","flow"]
print(longestCommonPrefix(strs))