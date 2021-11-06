mapper = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
roman = 'MIV'
res = 0

if 'IV' in roman:
    res += 4
    roman = roman.replace("IV", "&")    
if "IX" in roman:
    res += 9
    roman = roman.replace("IX", "&")    
if "XL" in roman:
    res += 40
    roman = roman.replace("XL", "&")    
if "XC" in roman:
    res += 90
    roman = roman.replace("XC", "&") 
if "CD" in roman:
    res += 400
    roman = roman.replace("CD", "&") 
if "CM" in roman:
    res += 900
    roman = roman.replace("CM", "&") 
for letter in roman:
    if letter in mapper:
        res += mapper[letter]
print(res)
