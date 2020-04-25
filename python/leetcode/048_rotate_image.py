#%%
"""
- Rotate Image
- https://leetcode.com/problems/rotate-image/
- Medium

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
"""

#%%
# 1. Up side down rotate: [i][:] --> [n-1-i][:]
# 2. diagonal rotate: [i][j] --> [j][i]
class S1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void, modify matrix in-place
        """
        n = len(matrix)
        # Up side down
        for i in range(n//2):
            matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
        
        # diagonal rotate
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


#%%
# Rotate four points together
# [x][y] --> [n-1-x][y] --> [y][n-1-x] --> [n-1-y][x]
class S2:
    def rotate(matrix):
        n = len(matrix)
        for i in range(n//2):
            for j in range(n-n//2):
                # [~i] == [n-1-i]
                matrix[i][j], matrix[~j][i], matrix[~i][~j], matrix[j][~i] = \
                    matrix[~j][i], matrix[~i][~j],matrix[j][~i], matrix[i][j]


#%%
# Pythonic zip
class S3:
    def rotate(matrix):
        matrix[:] = zip(*matrix[::-1])
        

#%%
