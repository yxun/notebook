#%%
"""
- Next Permutation
- https://leetcode.com/problems/next-permutation/
- Medium

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

#%%

# 1. From last digit to first, compare two digits until left one is less than right one.
# 2. If there is no left digit, this sequence has no next lexicographicall permutation.
# 3. Switch the left digit with the smallest one from right.
# 4. Reverse the right part.

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type: nums: List[int]
        :rtype: void do not return anything, modify nums in-place instead
        """
        if len(nums) <= 1:
            return
        idx = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]: # find first number which is smaller than it's after number
                idx = i
                break
        
        if idx != 0:
            for i in range(len(nums)-1, idx-1, -1):
                if nums[i] > nums[idx-1]:
                    nums[i], nums[idx-1] = nums[idx-1], nums[i]
                    break

        nums[idx:] = nums[idx:][::-1]


#%%
