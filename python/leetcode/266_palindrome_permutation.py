#%%
"""
- Palindrome Permutation
- https://leetcode.com/problems/palindrome-permutation/
- Easy
"""

#%%
"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

#%%
##
class S1:
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup = {}
        for c in s:
            if c not in lookup.keys():
                lookup[c] = 1
            elif c in lookup.keys():
                del lookup[c]
        
        if len(lookup.keys()) == 0 or len(lookup.keys()) == 1:
            return True
        else:
            return False