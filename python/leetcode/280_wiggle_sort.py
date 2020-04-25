#%%
"""
- Wiggle Sort
- https://leetcode.com/problems/wiggle-sort/
- Medium

Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""

#%%
##
class S1:
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None, modify nums in-place
        """
        if not nums: return

        nums2 = sorted(nums)
        l, r = 0, len(nums)-1

        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = nums2[l]
                l += 1
            else:
                nums[i] = nums2[r]
                r -= 1
        return
