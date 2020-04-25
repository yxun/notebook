#%%
"""
- Word Search
- https://leetcode.com/problems/word-search/
- Medium

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

#%%

# backtracking: Options, Restraints, Terminations

class S:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if len(board) == 0 or len(board[0]) == 0:
            return False

        used = [[0 for j in range(len(board[0]))] for i in range(len(board))]
        
        def dfs(i, j, k):
            if k == len(word):
                return True
            
            if i < 0 or i > len(board)-1 or j < 0 or j > len(board[0])-1:
                return False

            if board[i][j] == word[k] and not used[i][j]:
                used[i][j] = 1
                left = dfs(i-1,j,k+1)
                right = dfs(i+1,j,k+1)
                up = dfs(i,j-1,k+1)
                down = dfs(i,j+1,k+1)

                used[i][j] = left or right or up or down
                return left or right or up or down
            
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True

        return False

        
