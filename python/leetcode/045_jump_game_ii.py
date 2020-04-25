#%%
"""
- Jump Game II
- https://leetcode.com/problems/jump-game-ii/
- Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
"""

#%%
# greedy solution, the current jump is [i, cur_end], and the cur_farthest is the farthest point that all of point in [i, cur_end] can reach
# whenever cur_farthest is larger than the last point's index, return current jump+1
# whenever i reaches cur_end, update cur_end to cur_farthest.

# Time O(log(n)), Space O(1)

class S:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Note you can assume that you can always reach the last index.
        cur_end, cur_farthest, step, n = 0, 0, 0, len(nums)
        for i in range(n-1):
            cur_farthest = max(cur_farthest, i+nums[i])
            if cur_farthest >= n-1:
                step += 1
                break
            if i == cur_end:
                cur_end = cur_farthest
                step += 1
        return step


