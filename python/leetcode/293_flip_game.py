#%%
"""
- Flip Game
- https://leetcode.com/problems/flip-game/
- Easy
"""

#%%
"""
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

Example:

Input: s = "++++"
Output: 
[
  "--++",
  "+--+",
  "++--"
]
Note: If there is no valid move, return an empty list [].
"""

#%%
##
class S1:
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            if s[i] == '+' and s[i+1] == '+':
                l = s[:i]
                r = s[i+1:]
                res.append(l+"--"+r[1:])
        
        return res
                