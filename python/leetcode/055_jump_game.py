#%%
"""
- Jump Game
- https://leetcode.com/problems/jump-game/
- Medium

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

#%%
class S:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return True
        if len(nums) == 1:
            return True
        n = len(nums)
        idx, reach = 0, 0
        while idx < n-1 and idx <= reach:
            reach = max(reach, idx+nums[idx])
            idx += 1
        return reach >= n-1


#%%
