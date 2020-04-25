#%%
"""
- Multiply Strings
- https://leetcode.com/problems/multiply-strings/
- Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""

#%%
class S1:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0": return "0"

        m, n = len(num1), len(num2)
        pos = [0 for i in range(m+n)]

        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i+j, i+j+1
                s = mul + pos[p2]

                pos[p1] += s // 10
                pos[p2] = s % 10

        return ''.join(str(i) for i in pos).lstrip('0')

#%%
class S2:
    def multiply(self, num1, num2):
        product = 0
        num1, num2 = num1[::-1], num2[::-1]
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                product += int(n1) * int(n2) * 10**(i+j)
        
        return str(product)
