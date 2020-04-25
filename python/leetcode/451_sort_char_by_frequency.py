#%%
"""
- Sort Characters By Frequency
- https://leetcode.com/problems/sort-characters-by-frequency/
- Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
"""

#%%
##
class S1:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter
        d = sorted(Counter(s).items(), key=lambda x: x[1], reverse=True)
        result = ''
        for item in d:
            for i in range(item[1]):
                result += item[0]
        return result

#%%
class S2:
    def frequencySort(self, s):
        from collections import Counter
        count = Counter(s)
        res = ""
        for letter, c in count.most_common():
            res += letter*c
        return res