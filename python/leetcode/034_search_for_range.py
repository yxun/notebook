#%%
"""
- Search for a Range
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""

#%%
# binary search
# 1. find left boundary, nums[left] = target and (left == 0 or nums[left-1] != target)
# 2. check if we can find left boundary, if not, return [-1, -1]
# 3. find right boundary, nums[right] = target and (right == len(nums)-1 or nums[right+1] != target)

class S:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums: return [-1,-1]

        res = []
        l, r = 0, len(nums)-1

        # search for left bound
        while l <= r:
            mid = l + ((r-l) >> 2)
            if nums[mid] == target and (mid == 0 or nums[mid-1] != target):
                res.append(mid)
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        if not res:
            return [-1, -1]
        
        # search for right bound
        r = len(nums) - 1
        while l <= r:
            mid = l + ((r-l) >> 2)
            if nums[mid] == target and (mid == len(nums) - 1 or nums[mid+1] != target):
                res.append(mid)
                break
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return res
