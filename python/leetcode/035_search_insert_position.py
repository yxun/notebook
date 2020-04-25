#%%
"""
- Search Insert Position
- https://leetcode.com/problems/search-insert-position/
- Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""


#%%
##
class S1:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums: return 0
        
        res = 0
        l, r = 0, len(nums)-1
        
        while l < r:
            mid = l + ((r-l) >> 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        if nums[l] == target:
            return l
        elif nums[l] > target:
            return l
        else:
            return l+1


#%%
# simple solution, just find an element greater than or equal to target
class S2:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i = 0
        while nums[i] < target:
            i += 1
            if i == len(nums):
                return i
        return i


#%%
# binary search
class S3:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l) >> 2)
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return l
        