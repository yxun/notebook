#%%
"""
- Set Matrix Zeroes
- https://leetcode.com/problems/set-matrix-zeroes/
- Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

#%%
class S:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void, modify matrix in-place
        """
        def setZero(i,j):
            for m in range(col):
                matrix[i][m] = 0
            for n in range(row):
                matrix[n][j] = 0

        row = len(matrix)
        col = len(matrix[0]) if row else 0
        new_matrix = [matrix[i][:] for i in range(row)]

        for i in range(row):
            for j in range(col):
                if new_matrix[i][j] == 0:
                    setZero(i, j)
                    