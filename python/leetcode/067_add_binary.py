#%%
"""
- Add Binary
- https://leetcode.com/problems/add-binary/
- Easy

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

#%%
##
class S1:
    def addBinary(self, a, b):
        """
        :type a:str
        :type b:str
        :rtype: str
        """

        carry = 0
        i, j = len(a)-1, len(b)-1
        res = ""

        while i >= 0 and j >=0:
            num = int(a[i]) + int(b[j]) + carry
            carry = num // 2
            res = str(num%2) + res
            i -= 1
            j -= 1

        while i >= 0:
            num = int(a[i]) + carry
            carry = num // 2
            res = str(num%2) + res
            i -= 1
        
        while j >= 0:
            num = int(b[j]) + carry
            carry = num // 2
            res = str(num%2) + res
            j -= 1

        if carry:
            res = '1' + res
        
        return res

#%%
# recursion
class S2:
    def addBinary(self, a, b):
        if (a == '' or b == ''):
            return a + b
        elif a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            return self.addBinary(a[:-1], self.addBinary(b[:-1], '1')) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'
