#%%
"""
- Edit Distance
- https://leetcode.com/problems/edit-distance/
- Hard

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


#%%
# DP, dp[i][j] word1 0~i-1 chars and word2 0~j-1 chars
# if word1[i] == word2[j], dp[i][j] = dp[i-1][j-1]
# if word1[i] != word2[j], dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1  , deletion, insertion and replacement

class S1:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        matrix = [[i+j for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                if word1[i-1] == word2[j-1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)

        return matrix[len(word1)][len(word2)]


#%%
