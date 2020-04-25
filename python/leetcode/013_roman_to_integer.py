#%% [markdown]
'''
- Roman to Integer
- https://leetcode.com/problems/roman-to-integer/
- Easy

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
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


#%%
class S1:

    def romanToInteter(self, roman):
        """
        :type roman: str
        :rtype: int
        """

        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(roman)):
            if roman[i] not in ['I', 'X', 'C']:
                result += lookup[roman[i]]
            elif i == len(roman) - 1 :
                result += lookup[roman[i]]
            else:
                if roman[i] == 'I' and (roman[i+1] == 'V' or roman[i+1] == 'X'):
                    result -= 1
                elif roman[i] == 'X' and (roman[i+1] == 'L' or roman[i+1] == 'C'): 
                    result -= 10
                elif roman[i] == 'C' and (roman[i+1] == 'D' or roman[i+1] == 'M'): 
                    result -= 100
                else:
                    result += lookup[roman[i]]
        
        return result



#%%
from nose.tools import assert_equal

s = S1()
assert_equal(s.romanToInteter("III"), 3)
assert_equal(s.romanToInteter("IV"), 4)
assert_equal(s.romanToInteter("IX"), 9)
assert_equal(s.romanToInteter("LVIII"), 58)
assert_equal(s.romanToInteter("MCMXCIV"), 1994)
print('Success')

#%%
