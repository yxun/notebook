#%%
'''
- 3 Sum
- https://leetcode.com/problems/3sum/
- Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

#%%
class S1:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def twoSum(nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: List[int]
            """

            lookup = {}
            for num in nums:
                if target-num in lookup:
                    if (-target, target-num, num) not in res:
                        res.append((-target, target-num, num))
                lookup[num] = target - num

        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            twoSum(nums[i+1:], 0-nums[i])
        return [list(i) for i in res]


#%%
"""
# Good solution
- Sort
- Fix left item, if it is duplicate, continue
- Move left and right points, remove duplicates and process left and right
"""

class S2:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n, res = len(nums), []
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif tmp > 0:
                    r -= 1
                else:
                    l += 1
        return res


#%%
from nose.tools import assert_equal

s = S1()
nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1,0,1],[-1,-1,2]]
assert_equal(s.threeSum(nums),expected)

s = S2()
nums = [-1, 0, 1, 2, -1, -4]
expected = [[-1,-1,2], [-1,0,1]]
assert_equal(s.threeSum(nums),expected)

print('Success')

#%%
