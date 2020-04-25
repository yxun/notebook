#%%
"""
- Max Consecutive Ones
- https://leetcode.com/problems/max-consecutive-ones/
- Easy

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
"""

#%%
##
class S1:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0

        res = 0
        count = 0

        for i in range(len(nums)):
            if nums[i] == 1 and i != len(nums)-1:
                count += 1
            elif nums[i] == 1 and i == len(nums)-1:
                count += 1
                res = max(res, count)
            else:   # nums[i] == 0
                res = max(res, count)
                count = 0
        return res

#%%
class S2:
    def findMaxConsecutiveOnes(self, nums):
        return len(max(''.join(map(str, nums)).split('0')))

#%%
class S3:
    def findMaxConsecutiveOnes(self, nums):
        res, count = [], 0
        for x in nums:
            count = 0 if x == 0 else count + 1
            res.append(count)
        return max(res)
        