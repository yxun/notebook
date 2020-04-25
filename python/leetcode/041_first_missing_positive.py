#%%
"""
- First Missing Positive
- https://leetcode.com/problems/first-missing-positive/description/
- Hard

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.
"""

#%%
##
class S1:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        
        lookup = [ 0 for i in range(len(nums))]  # lookup represents [1, 2, 3... len(nums)]
        
        for i in range(len(nums)):
            if nums[i] > 0 and nums[i] <= len(nums):
                lookup[nums[i]-1] += 1
        
        
        for j in range(len(lookup)):
            if lookup[j] == 0:
                return j+1
            if j == len(lookup)-1 and lookup[j] != 0:
                return len(nums)+1
        

#%%
s = S1()
nums = [2,1]
s.firstMissingPositive(nums)


#%%
class S2:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        old_missing, missing = 0, 1
        while old_missing != missing:
            old_missing = missing
            for i in range(len(nums)):
                if nums[i] == missing:
                    missing += 1
        return missing


#%%
class S3:
    def firstMissingPositive(self, nums):
        if not nums:
             return 1
        lookup = {}
        for n in nums:
            lookup[n] = 1
        if max(nums) <= 0:
            return 1
        for m in range(1, max(nums) + 2):
            if m not in lookup:
                return m