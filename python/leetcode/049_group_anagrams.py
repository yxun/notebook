#%%
"""
- Group Anagrams
- https://leetcode.com/problems/group-anagrams/
- Medium

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

#%%
class S:

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        lookup = {}
        for n in strs:
            key = ''.join(sorted(list(n)))
            if key in lookup:
                lookup[key].append(n)
            else:
                lookup[key] = [n]
        return lookup.values()
      

#%%
