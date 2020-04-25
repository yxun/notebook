#%%
"""
- Substring with Concatenation of All Words
- https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
- Hard

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

 

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""


#%%
import collections

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        if len(words) == 0 or len(s) < len(words) * len(words[0]):
            return res
        n, m, wl = len(s), len(words), len(words[0])
        maps, cur_map = {}, {}
        maps  = collections.Counter(words)
        for i in range(wl):
            count, start, r = 0, i, i
            while r + wl <= n:
                string = s[r:r+wl]
                if string in maps:
                    cur_map[string] = cur_map.get(string,0) + 1
                    if cur_map[string] <= maps[string]:
                        count += 1
                    while cur_map[string] > maps[string]:
                        tmp = s[start:start+wl]
                        cur_map[tmp] -= 1
                        start += wl
                        if cur_map[tmp] < maps[tmp]:
                            count -= 1
                    if count == m:
                        res.append(start)
                        tmp = s[start:start+wl]
                        cur_map[tmp] -= 1
                        start += wl
                        count -= 1
                else:
                    cur_map = {}
                    count = 0
                    start = r + wl
                r += wl
            cur_map = {}
        return res


#%%
