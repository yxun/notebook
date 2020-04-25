#%%
"""
- Regular Expression Matching
- https://leetcode.com/problems/regular-expression-matching/
- Hard

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""


#%%
class S1:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        def helper(s, i, p, j):
            if j == -1:
                return i == -1
            if i == -1:
                if p[j] != '*':
                    return False
                return helper(s, i, p, j-2)

            if p[j] == '*':
                if p[j-1] == '.' or p[j-1] == s[i]:
                    if helper(s, i-1, p, j):
                        return True
                return helper(s, i, p, j-2)

            if p[j] == '.' or p[j] == s[i]:
                return helper(s, i-1, p, j-1)
            return False

        return helper(s, len(s)-1, p, len(p)-1)

s = 'abc'
p = 'a*abc'
ss = S1()
print(ss.isMatch(s, p))


#%%
# DP
class S2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        m, n = len(s), len(p)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        dp[0][0] = 1

        # init the first line
        for i in range(2, n+1):
            if p[i-1] == '*':
                dp[0][i] == dp[0][i-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    if p[j-2] != s[i-1] and p[j-2] != '.':
                        dp[i][j] = dp[i][j-2]
                    elif p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] =  dp[i-1][j] or dp[i][j-2]
                
                elif s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]


        return dp[m][n] == 1


ss = S1()
s = "aab"
p = "c*a*b"
print(ss.isMatch(s, p))


s = ""
p = "c*a"
print(ss.isMatch(s, p))

