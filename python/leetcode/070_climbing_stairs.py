#%%
"""
- Climbing Stairs
- https://leetcode.com/problems/climbing-stairs/
- Easy

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

#%%
# This is a Fibonacci problem + one step forward. dp[n] = dp[n-1] + dp[n-2]

# DP1, top-down
class S1:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fibonacci memo = {1:1, 2:1}
        memo = {1:1, 2:2}   # climb stairs, 1,2,3,5; fibonacci first three, 1,1,2,3,5
        if n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
            return memo[n]

#%%
# DP2, bottom up
# Time complexity O(n), Space complexity O(1)

class S2:
    def climbStairs(self, n):
        # fibonacci fib = [1, 1, 2]
        fib = [1, 2, 3] # climb stairs
        if n < 4:
            return fib[n-1]
        for k in range(3, n+1):
            fib[2] = fib[0] + fib[1]
            fib[0], fib[1] = fib[1], fib[2]
        return fib[2]

#%%
# math
# Time complexity O(lg(n)), space complexity O(1)

class S3:
    def climbStairs(self, n):
        import math
        sqrt5 = math.sqrt(5)
        fibn = pow((1+sqrt5) / 2, n+1) - pow((1-sqrt5) / 2, n+1)
        return int(float(fibn/sqrt5))
