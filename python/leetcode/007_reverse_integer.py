#%%
'''
- Reverse Integer
- https://leetcode.com/problems/Reverse-Integer
- Easy
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
'''

#%%
class S1:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        flag = 1
        x_1 = 0
        if x < 0:
            flag = -1
            x = int(str(abs(x))[::-1])
            x_1 = x * flag
        else:
            flag = 1
            x = int(str(x)[::-1])
            x_1 = x * flag
        
        # check if overflow
        if x_1 > 2 ** 31 -1 or x_1 < -2 ** 31:
            return 0
        else:
            return x_1

s = S1()
x = 120
y = -456
print(s.reverse(x))
print(s.reverse(y))

#%%
class S2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        flag = 1
        if x > 0:
            flag = 1
        else:
            flag = -1
        while x != 0:
            num = num * 10 + x % (10 * flag)
            x = int(x / 10)   # use x // 10 is wrong. because -12.2 // 10 = -13
        if num > 2**31-1 or num < -2**31:
            return 0
        else:
            return num

s = S2()
x = 120
y = -456
print(s.reverse(x))
print(s.reverse(y))

#%%
