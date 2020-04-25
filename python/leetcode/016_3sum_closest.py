#%%
"""
- 3 Sum Closest
- https://leetcode.com/problems/3sum-closest/
- Medium

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

#%%
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :rtype: int
        """

        n, res, diff = len(nums), None, float('inf')
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return target
                elif tmp > target:
                    r -= 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                else:
                    l += 1
                    if abs(tmp-target) < diff:
                        diff = abs(tmp-target)
                        res = tmp
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res



#%%
from nose.tools import assert_equal

s = Solution()
nums = [-1, 2, 1, -4]
target = 1
expected = 2
assert_equal(s.threeSumClosest(nums, target), expected)
print('Success')


#%%
