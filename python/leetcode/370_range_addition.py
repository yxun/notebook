#%%
"""
- Range Addition
- https://leetcode.com/problems/range-addition/
- Medium
"""

#%%
"""
Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet: [startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:

Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
Output: [-2,0,3,5,3]
Explanation:

Initial state:
[0,0,0,0,0]

After applying operation [1,3,2]:
[0,2,2,2,0]

After applying operation [2,4,3]:
[0,2,5,5,3]

After applying operation [0,2,-2]:
[-2,0,3,5,3]
"""

#%%
class S1:
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        arr = [0 for _ in range(length+1)]
        for start, end, inc in updates:
            arr[start] += inc
            arr[end+1] -= inc
        
        for i in range(1, length+1):
            arr[i] = arr[i] + arr[i-1]
        return arr[:-1]
