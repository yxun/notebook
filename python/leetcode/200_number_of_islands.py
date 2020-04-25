#%%
"""
- Number of Islands
- https://leetcode.com/problems/number-of-islands/
- Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

#%%
class S1:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        row = len(grid)
        col = len(grid[0]) if row else 0
        used = [[0 for i in range(col)] for i in range(row)]

        def dfs(x, y):
            if grid[x][y] == '0' or used[x][y]:
                return
            used[x][y] = 1

            if x != 0:
                dfs(x-1, y)
            if x != row-1:
                dfs(x+1, y)
            if y != 0:
                dfs(x, y-1)
            if y != col-1:
                dfs(x, y+1)

        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and not used[i][j]:
                    dfs(i, j)
                    res += 1
        return res

#%%
# Sink and count
class S2:
    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == '1':
                grid[i][j] = '0'
                list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
                return 1
            return 0
        
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[0])))
