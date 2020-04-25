#%%
"""
- Sort Colors
- https://leetcode.com/problems/sort-colors/description/
- Medium

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""

#%%
# two passes, count color first and then set value

class S1:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void, modify nums in-place
        """
        red, white, blue = 0, 0, 0
        for i in nums:
            if i == 0:
                red += 1
            elif i == 1:
                white += 1
        
        for i in range(red):
            nums[i] = 0
        for i in range(red, red+white):
            nums[i] = 1
        for i in range(red+white, len(nums)):
            nums[i] = 2


#%%
# two pointers

class S2:
    def sortColors(self, nums):
        i, l, r = 0, 0, len(nums)-1
        while i < len(nums):
            if nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], 2
                r -= 1
            elif nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], 0
                l += 1
            else:
                i += 1

#%%
class S3:
    def sortColors(self, nums):
        n0, n1, n2 = -1, -1, -1
        for i in range(len(nums)):
            if nums[i] == 0:
                n0, n1, n2 = n0+1, n1+1, n2+1
                nums[n2] = 2
                nums[n1] = 1
                nums[n0] = 0
            elif nums[i] == 1:
                n1, n2 = n1+1, n2+1
                nums[n2] = 2
                nums[n1] = 1
            else:
                n2 += 1
                nums[n2] = 2
                