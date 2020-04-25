#%%
"""
- Maximum Subarray
- https://leetcode.com/problems/maximum-subarray/
- Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

#%%
# from i , calculate i to n
# O(n^2)

class S1:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        m = float('-inf')
        for i in range(n):
            s = 0
            for j in range(i, n):
                s += nums[j]
                m = max(m, s)
        return m

#%%
# DP
# ms(i) = max(ms[i]+a[i], a[i])
# at index i , the max range may be in either adding a[i] or start from a[i]

class S2:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxSum = [nums[0] for i in range(n)]
        for i in range(1,n):
            maxSum[i] = max(maxSum[i-1] + nums[i], nums[i])
        return max(maxSum)


#%%
class S3:

    def maxSubArray(self, nums):
        n = len(nums)
        maxSum, maxEnd = nums[0], nums[0]

        for i in range(1, n):
            maxEnd = max(nums[i], maxEnd + nums[i])
            maxSum = max(maxEnd, maxSum)
        return maxSum


#%%
# Divide and Conquer
# The max subarray sum has three options: left part, right part or across left and right part
# O(nlogn)
class S4:

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def find_max_crossing_subarray(nums, low, mid, high):
            left_sum = float('-inf')
            sum = 0
            for i in range(mid, low-1, -1):
                sum = sum + nums[i]
                if sum > left_sum:
                    left_sum = sum

            right_sum = float('-inf')
            sum = 0
            for j in range(mid+1, high+1):
                sum = sum + nums[j]
                if sum > right_sum:
                    right_sum = sum
            
            return left_sum + right_sum
        

        def find_max_subarray(nums, low, high):
            if low == high:
                return nums[low]
            else:
                mid = (low+high) // 2
                left_sum = find_max_subarray(nums, low, mid)
                right_sum = find_max_subarry(nums, mid+1, high)
                cross_sum = find_max_crossing_subarray(nums, low, mid, high)
                return max(left_sum, right_sum, cross_sum)

        return find_max_subarray(nums, 0, len(nums)-1)        


#%%
