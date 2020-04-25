#%%
"""
- Spiral Matrix
- https://leetcode.com/problems/spiral-matrix/
- Medium

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

#%%
class S1:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(list(zip(*matrix))[::-1])


#%%
class S2:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []

        res = []
        maxUp = maxLeft = 0
        maxDown = len(matrix)-1
        maxRight = len(matrix[0])-1
        direction = 0   # 0 go right, 1 go down, 2 go left, 3 up
        while True:
            if direction == 0:
                for i in range(maxLeft, maxRight+1):
                    res.append(matrix[maxUp][i])
                maxUp += 1
            elif direction == 1:
                for i in range(maxUp, maxDown+1):
                    res.append(matrix[i][maxRight])
                maxRight -= 1
            elif direction == 2:
                for i in reversed(range(maxLeft, maxRight+1)):
                    res.append(matrix[maxDown][i])
                maxDown -= 1
            else:
                for i in reversed(range(maxUp, maxDown+1)):
                    res.append(matrix[i][maxLeft])
                maxLeft += 1
            if maxUp > maxDown or maxLeft > maxRight:
                return res

            direction = (direction + 1) % 4


#%%
