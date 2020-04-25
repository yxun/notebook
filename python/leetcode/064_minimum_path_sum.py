#%%
"""
- Minimum Path Sum
- https://leetcode.com/problems/minimum-path-sum
- Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

#%%
##
# DP, dp[i,j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j], 
# dp[0][j] = dp[0][j-1] + grid[0,j], 
# dp[i][0] = dp[i-1][0] + grid[i][0]

class S1:
    def minPathSum(self, grid):
        """
        :type: grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0

        dp = [[0] * len(grid[0]) for i in range(len(grid))]
        m,n = len(grid[0]), len(grid)
        dp[0][0] = grid[0][0]

        for i in range(n):
            for j in range(m):
                if i == 0 and j > 0:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    #dp[i][j] = sum(grid[i][k] for k in range(j+1))
                elif j == 0 and i > 0:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    #dp[i][j] = sum(grid[k][j] for k in range(i+1))
                elif i > 0 and j > 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

        return dp[n-1][m-1]
                    

