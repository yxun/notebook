#%%
"""
- N-Queens II
- https://leetcode.com/problems/n-queens-ii/
- Hard
"""

#%%
class S:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        # col_per_row: every row the Queens colum indexes
        # cur_row: current row index
        # xy_diff: x-y
        # xy_sum: x+y

        def dfs(col_per_row, xy_diff, xy_sum):
            cur_row = len(col_per_row)
            if cur_row == n:
                ress.append(col_per_row)
            for col in range(n):
                if col not in col_per_row and cur_row - col not in xy_diff and cur_row + col not in xy_sum:
                    dfs(col_per_row + [col], xy_diff+[cur_row-col], xy_sum+[cur_row+col])
            
        ress = []
        dfs([], [], [])
        return len(ress)
