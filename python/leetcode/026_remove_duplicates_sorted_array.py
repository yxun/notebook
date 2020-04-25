#%%
"""
- Remove Duplicates from Sorted Array
- https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- Easy

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
"""


#%%
class S:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < (len(nums) -1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)



#%%
