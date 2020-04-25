#%% 
from nose.tools import assert_equal

#%% [markdown]
'''
- Longest Palindromic Substring
- https://leetcode.com/problems/longest-palindromic-substring/
- Medium
'''

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

#%%
class S1:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        m,l,r = 0,0,0   # m length of the current longest palindromic substring; l left index; r right index

        for i in range(n):
            # odd case
            for j in range(min(i+1, n-i)):
                if s[i-j] != s[i+j]:
                    break
                if 2*j + 1 > m:
                    m = 2*j + 1
                    l = i-j
                    r = i+j
            
            # even case
            if i+1 < n and s[i] == s[i+1]:
                for j in range(min(i+1, n-i-1)):
                    if s[i-j] != s[i+j+1]:
                        break
                    if 2*j + 2 > m:
                        m = 2*j + 2
                        l = i-j
                        r = i+j+1
        
        return s[l:r+1]


#%%
s = S1()
nums = "acbcd"
expected = "cbc"
assert_equal(s.longestPalindrome(nums), expected)

nums = "acbd"
expected = "a"
assert_equal(s.longestPalindrome(nums), expected)

nums = "abcggxcba"
expected = "gg"
assert_equal(s.longestPalindrome(nums), expected)

print('Success')

#%%
class S2():

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def lcs(s1, s2):
            m = [[0] * (1 + len(s2)) for i in range(1 + len(s1))]
            longest, x_longest = 0, 0
            for x in range(1, 1 + len(s1)):
                for y in range(1, 1 + len(s2)):
                    if s1[x-1] == s2[y-1]:
                        m[x][y] = m[x-1][y-1] + 1
                        if m[x][y] > longest:
                            tmp = s1[x-m[x][y]:x]
                            if tmp == tmp[::-1]:
                                longest = m[x][y]
                                x_longest = x
                    else:
                        m[x][y] = 0
            return s1[x_longest - longest: x_longest]

        return lcs(s, s[::-1])

#%%
s = S2()
nums = "acbcd"
expected = "cbc"
assert_equal(s.longestPalindrome(nums), expected)

nums = "acbd"
expected = "a"
assert_equal(s.longestPalindrome(nums), expected)

nums = "abcggxcba"
expected = "gg"
assert_equal(s.longestPalindrome(nums), expected)

print('Success')

#%%
# Manacher algorithm
