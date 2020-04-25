#%%
"""
- Minimum Window Substring
- https://leetcode.com/problems/minimum-window-substring/
- Hard

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

#%%
class S:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        import collections

        if len(t) > len(s):
            return ''
        
        maps = collections.Counter(t)
        counter = len(maps.keys())
        begin, end, head, length = 0, 0, 0, float('inf')
        
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if s[begin] in maps:
                    maps[s[begin]] += 1
                    if maps[s[begin]] > 0:
                        counter += 1
                if end - begin < length:
                    length = end - begin
                    head = begin
                begin += 1

        if length == float('inf'):
            return ''
        
        return s[head:head+length]
        