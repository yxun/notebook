#%%
"""
- Longest Valid Parentheses
- https://leetcode.com/problems/longest-valid-parentheses
- Hard

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


#%%
# find the index of ) which can be paired with ( and then calculate the longest valid substring.

class S1:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    continue
            stack.append(i)
        
        max_length = 0
        next_index = len(s)

        while stack:
            cur_index = stack.pop()
            cur_length = next_index - cur_index - 1
            max_length = max(cur_length, max_length)
            next_index = cur_index

        return max(next_index, max_length)


#%%
s = S1()
print(s.longestValidParentheses("()(())"))
print(s.longestValidParentheses("()()(()"))

#%%
# DP, dp[x] = y means at index x, the longest valid substring length is y
# so if s[i] == '(', dp[i] = dp[i-1] + 0
# if s[i] == ')' and there is a '(' before dp[i-1], dp[i] = dp[i-1] + 2 and possiblely combine dp[left-1].

class S2:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        if len(s) == 0:
            return 0
        dp = [0 for i in range(len(s))]
        for i in range(1, len(s)):
            if s[i] == ')':
                left = i - 1 - dp[i-1]
                if left >= 0 and s[left] == '(':
                    dp[i] = dp[i-1] + 2
                    if left > 0:
                        dp[i] += dp[left-1]
        return max(dp)
        

#%%
s = S2()
print(s.longestValidParentheses("()(())"))
print(s.longestValidParentheses("()()(()"))

#%%
