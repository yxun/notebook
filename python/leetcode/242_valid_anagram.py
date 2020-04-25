#%%
"""
- Valid Anagram
- https://leetcode.com/problems/valid-anagram/
- Easy

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
"""

#%%
class S1:
    def isAnagram(self, s, t):
        import collections
        return collections.Counter(s) == collections.Counter(t)

#%%
class S2:
    def isAnagram(self, s, t):
        return sorted(s) == sorted(t)

#%%
class S3:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        charCnt = [0]*26

        for i in range(len(s)):
            charCnt[ord(s[i])-97] += 1
            charCnt[ord(t[i])-97] -= 1

        for cnt in charCnt:
            if cnt != 0:
                return False
        return True
        