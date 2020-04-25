#%%
from nose.tools import assert_equal

#%% [markdown]
'''
- Longest Substring Without Repeating Characters
- https://leetcode.com/problems/longest-substring-without-repeating-characters/
- Medium
'''

'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#%%
class S1:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l, start, n = 0, 0, len(s)
        maps = {}
        for i in range(n):
            start = max(start, maps.get(s[i], -1)+1)
            l = max(l, i-start+1)
            maps[s[i]] = i
        return l


#%%
t1 = "abcabcbb"
t2 = "bbbbb"
t3 = "pwwkew"
s = S1()
expected = 3
assert_equal(s.lengthOfLongestSubstring(t1), expected)
expected = 1
assert_equal(s.lengthOfLongestSubstring(t2), expected)
expected = 3
assert_equal(s.lengthOfLongestSubstring(t3), expected)
print('Success')

#%%
