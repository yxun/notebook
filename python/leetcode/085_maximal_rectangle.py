#%%
"""
- Maximal Rectangle
- https://leetcode.com/problems/maximal-rectangle/
- Hard

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

#%%
class S:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0
        
        n = len(matrix[0])
        heights = [0]*n
        heights.append(0)   # to spit out the stack in the end
        ans = 0

        for k in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if matrix[k][j] == "1" else 0
            i = 0
            stack = []
            while i <= n:
                if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                    i += 1
                else:
                    top = stack.pop()
                    if len(stack) != 0:
                        area = heights[top]*(i-1-stack[-1])
                    else:
                        area = heights[top]*(i-1+1)
                    ans = max(area,ans)
        return ans
