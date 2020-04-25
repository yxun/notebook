#%%
"""
- Subsets
- https://leetcode.com/problems/subsets/description/
- Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

#%%
class S1:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res.extend([tmp+[num] for tmp in res])
        return res

#%%
# BackTrack
# For each element, there are only two choices. Either add the element into cur_lst or not add it.

class S2:
    def subsets(self, nums):
        nums.sort()
        res = []

        def search(cur_lst, idx):
            if idx == len(nums):
                res.append(cur_lst)
                return
            search(cur_lst + [nums[idx]], idx+1)
            search(cur_lst, idx + 1)
        
        search([], 0)
        return res

#%%
# DFS

class S3:
    def subsets(self, nums):
        nums.sort()
        res = []

        def dfs(depth, start, lst):
            res.append(lst)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, lst+[nums[i]])
        dfs(0, 0, [])
        return res
        