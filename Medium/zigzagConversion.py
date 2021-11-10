'''
The string "PAYPALISHIRING" is written in a zigzag pattern 
on a given number of rows like this: 
(you may want to display this pattern in a fixed font 
for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion 
given a number of rows:

string convert(string s, int numRows);
'''


s = "PAYPALISHIRING"
numRows = 4
def convert(s: str, numRows: int) -> str:
    if numRows == 1:
        return s
    if len(s) <= numRows:
        return s
    chunks = ['{}'.format(s[x]) for x in range(numRows)]
    s = s[numRows:]
    toggle = True
    while s:
        try:
            if toggle:
                for i in reversed(range(len(chunks)-1)):
                    chunks[i] += s[0] 
                    s = s[1:]
                    toggle = False
            else:
                for i in range(1, len(chunks)):
                    chunks[i] += s[0] 
                    s = s[1:]
                    toggle = True
        except:
            pass
    result = "".join(chunks)
    return result
print(convert(s, numRows))