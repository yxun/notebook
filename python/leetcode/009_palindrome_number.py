#%%
"""
- Palindrome Number
- https://leetcode.com/problems/palindrome-number
- Easy

Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""


#%%
class S1:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False
        elif x != int(str(x)[::-1]):
            return False
        else:
            return True

s = S1()
x = 2345
y = 121
print(s.isPalindrome(x))
print(s.isPalindrome(y))


#%%
class S2:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0 or (x % 10 == 0 and x is not 0):
            return False

        revertNumber = 0
        while x > revertNumber:
            revertNumber = revertNumber * 10 + x % 10
            x /= 10

        # if length of number is odd, use revertNumber/10 to remove the medium
        return x == revertNumber or x == revertNumber / 10

s = S2()
x = 2345
y = 121
print(s.isPalindrome(x))
print(s.isPalindrome(y))


#%%
