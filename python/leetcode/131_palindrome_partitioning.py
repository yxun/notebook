#%%
"""
- Palindrome Partitioning
- https://leetcode.com/problems/palindrome-partitioning/
- Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

#%%
# back-tracking
class S1:

    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.dfs(s, [])
        return self.res

    def dfs(self, s: str, cur: List[str]) -> None:
        if len(s) == 0:
            self.res.append(cur)
            return
        
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:
                self.dfs(s[i:], cur+[s[:i]])
