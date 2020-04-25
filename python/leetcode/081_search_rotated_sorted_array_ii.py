#%%
"""
- Search in Rotated Sorted Array II
- https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
- Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

#%%

class S1:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l)//2)
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:
                if nums[l] <= target <= nums[mid]:      # non-rotated
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid] < nums[l]:
                if nums[mid] <= target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                l += 1
        return False
