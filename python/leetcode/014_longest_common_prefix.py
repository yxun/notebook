#%%
'''
- 14. Longest Common Prefix
- https://leetcode.com/problems/longest-common-prefix/
- Easy

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''

#%%
class S1:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List(str)
        :rtype: str
        """

        if not strs:
            return ""
        
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]

        return strs[0]


s = S1()
s.longestCommonPrefix(['laa', 'lab', 'lac'])
#%%
import os

class S2:
    def longestCommonPrefix(self, strs):
        return os.path.commonprefix(strs) 