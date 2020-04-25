#%%
from nose.tools import assert_equal

#%% [markdown]
'''
- Two Sum
- https://leetcode.com/problems/two-sum/
- Easy
'''

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
#%%
class S1(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num_one in nums:
            if target-num_one in nums and num_one is not target-num_one:
                return [nums.index(num_one), nums.index(target-num_one)]

#%%
nums = [4, 3, 5, 15]
target = 8
s = S1()
expected = [1, 2]
assert_equal(s.twoSum(nums, target), expected)
print('Success')

#%%
class S2(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num], i]
            lookup[num] = i
        return []


#%%
nums = [4 ,3 ,5 , 15]
target = 8
s = S2()
expected = [1, 2]
assert_equal(s.twoSum(nums, target), expected)
print("Success")


