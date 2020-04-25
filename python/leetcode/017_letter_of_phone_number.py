#%%
'''
- Letter Combinations of a Phone Number
- https://leetcode.com/problems/letter-combinations-of-a-phone-number/
- Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''


#%%
class S:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = ['']
        for c in digits:
            tmp = []
            for letter in lookup[c]:
                tmp.extend([pre + letter for pre in result])
            result = tmp
        return sorted(result) if result != [''] else []


#%%
from nose.tools import assert_equal

s = S()
digits = "23"
expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
assert_equal(s.letterCombinations(digits), expected)
print('Success')

#%%
