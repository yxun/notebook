#%%
"""
- Valid Sudoku
- https://leetcode.com/problems/valid-sudoku/
- Medium

Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
"""

#%%
##
class S1:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board:
            return False

        row_lookup = []
        col_lookup = [[] for i in range(10)]
        t_lookup = [[] for i in range(3)]

        for y in range(len(board)):
            row_lookup = []
            if y % 3 == 0:
                t_lookup = [[] for i in range(3)]
            for x in range(len(board[y])):
                value = board[y][x]
                if value == ".":
                    continue
                elif value in row_lookup or value in t_lookup[x // 3] or value in col_lookup[x]:
                    return False
                else:
                    row_lookup.append(value)
                    t_lookup[x // 3].append(value)
                    col_lookup[x].append(value)
        
        return True
                
        
       




#%%
s = S1()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
s.isValidSudoku(board)


#%%
