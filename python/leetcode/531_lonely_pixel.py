#%%
"""
- Lonely Pixel I
- https://leetcode.com/problems/lonely-pixel-i/
- Medium
"""

#%%
"""
Given a picture consisting of black and white pixels, find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W', which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position where the same row and same column don't have any other black pixels.

Example:

Input: 
[['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
Note:

The range of width and height of the input 2D array is [1,500].

"""

#%%
class S1:
    def findLonelyPixel(self, picture):
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B') for col in zip(*picture))
        