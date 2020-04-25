#%% [markdown]
"""
- Integer to Roman
- https://leetcode.com/problems/integer-to-roman/
- Medium

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"
Example 2:

Input: 4
Output: "IV"
Example 3:

Input: 9
Output: "IX"
Example 4:

Input: 58
Output: "LVIII"
Explanation: L = 50, V = 5, III = 3.
Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


#%%
class S1:
    def intToRoman(self, num: int) -> str:
        
        symbols = [
            ('M', 1000), 
            ('D', 500), 
            ('C', 100), 
            ('L', 50),
            ('X', 10),
            ('V', 5),
            ('I', 1)
        ]
        
        result = ""
        
        while num > 0:
            for s in symbols:
                if num >= s[1]:
                    result += s[0]*(num // s[1])
                    num %= s[1]
        
        result = result.replace("DCCCC", "CM")
        result = result.replace("CCCC", "CD")
        result = result.replace("LXXXX", "XC")
        result = result.replace("XXXX", "XL")
        result = result.replace("VIIII", "IX")
        result = result.replace("IIII", "IV")
                
        return result

#%%
class S2:
    def intToRoman(self, num: int) -> str:
        
        symbols = [
            ('M', 1000), 
            ('CM', 900),
            ('D', 500),
            ('CD', 400), 
            ('C', 100),
            ('XC', 90),
            ('L', 50),
            ('XL', 40),
            ('X', 10),
            ('IX', 9),
            ('V', 5),
            ('IV', 4),
            ('I', 1)
        ]
        
        result = ""
        
        for s in symbols:
            while num >= s[1]:
                result += s[0]
                num -= s[1]
                
        return result

#%%
from nose.tools import assert_equal

s = S1()
pair = [(3, "III"), (4, "IV"), (9, "IX"), (58, "LVIII"), (1994, "MCMXCIV")]

for p in pair:
    assert_equal(s.intToRoman(p[0]), p[1])

s = S2()
for p in pair:
    assert_equal(s.intToRoman(p[0]), p[1])

print('Success')

#%%
