#%%
'''
- Valid Parentheses
- https://leetcode.com/problems/valid-parentheses
- Easy

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

#%%
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        leftP = '([{'
        rightP = ')]}'
        stack = []
        for char in s:
            if char in leftP:
                stack.append(char)
            if char in rightP:
                if not stack:
                    return False
                tmp = stack.pop()
                if char == ')' and tmp != '(':
                    return False
                if char == ']' and tmp != '[':
                    return False
                if char == '}' and tmp != '{':
                    return False
        return stack == []


#%%
s = Solution()
print(s.isValid("([[])[]{}"))
print(s.isValid("([])[]{}"))

#%%
