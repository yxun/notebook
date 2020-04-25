#%%
"""
- Palindrome Partitioning II
- https://leetcode.com/problems/palindrome-partitioning-ii/
- Hard

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

#%%
# cut[i] : the minimum cut needed for the first i characters
# dp[j][i] : whether s[j] to s[i] is palindrome (inclusive)
class S1:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [-1] + [n]*n
        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (j+1>=i or dp[j+1][i-1]):
                    dp[j][i] = True
                    cut[i+1] = min(cut[i+1], cut[j]+1)
        return cut[-1]

#%%
# dp[j][i] only depends on the results of previous column dp[j+1][i-1]
class S2:
    def minCut(self, s: str) -> int:
        n = len(s)
        cut = [-1] + [n]*n
        dp = [False] * n
        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j] and (j+1>=i or dp[j+1]):
                    dp[j] = True
                    cut[i+1] = min(cut[i+1], cut[j]+1)
                else:
                    dp[j] = False
        return cut[-1]
        