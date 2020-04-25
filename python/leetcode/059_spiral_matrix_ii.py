#%%
"""
- Spiral Matrix II
- https://leetcode.com/problems/spiral-matrix-ii/
- Medium

Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

#%%

class S1:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[n*n]]
        low = n*n
        while low > 1:
            low, high = low - len(res), low
            res = [[i for i in range(low,high)]] + list(zip(*res[::-1]))
        return res

#%%
class S2:
    def generateMatrix(self, n):
        curNum = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        maxUp = maxLeft = 0
        maxDown = maxRight = n-1
        direction = 0
        while True:
            if direction == 0:  # go right
                for i in range(maxLeft, maxRight+1):
                    curNum += 1
                    matrix[maxUp][i] = curNum
                maxUp += 1
            elif direction == 1:    # go down
                for i in range(maxUp, maxDown+1):
                    curNum += 1
                    matrix[i][maxRight] = curNum
                maxRight -= 1
            elif direction == 2:    # go left
                for i in reversed(range(maxLeft, maxRight+1)):
                    curNum += 1
                    matrix[maxDown][i] = curNum
                maxDown -= 1
            else:   # go up
                for i in reversed(range(maxUp, maxDown+1)):
                    curNum += 1
                    matrix[i][maxLeft] = curNum
                maxLeft += 1
            if curNum >= n*n:
                return matrix
            direction = (direction + 1) % 4

#%%