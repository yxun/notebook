#%%
"""
- Pow(x,n)
- https://leetcode.com/problems/powx-n/
- Medium

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
"""
#%%
# recursion is faster than iterative

class S:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            x = 1/x
        
        pow = self.myPow(x, abs(n)//2)
        if n % 2 == 0:
            return pow * pow
        else:
            return x * pow * pow

#%%
