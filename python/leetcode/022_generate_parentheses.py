#%%
"""
- Generate Parentheses
- https://leetcode.com/problems/generate-parentheses/
- Medium

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

#%%
# backtrack

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.res = []
        self.singleStr('', 0, 0, n)
        return self.res

    def singleStr(self, s, left, right, n):
        if left == n and right == n:
            self.res.append(s)
        if left < n:
            self.singleStr(s + '(', left + 1, right, n)
        if right < left:
            self.singleStr(s + ')', left, right + 1, n)


#%% [markdown]
"""
## backtracking
In some situation, you have some options to choose. Find all the combinateions within certain restraints.

### Three points
- Options
- Restraints
- Termination

### This example
Options:
1. add (
2. add )

Restraints:
1. left <= n
2. right < left

Termination:
left == right == n

"""

#%%
