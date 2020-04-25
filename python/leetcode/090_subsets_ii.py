#%%
"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# %%
# backtrack
class S1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def search(curlist: List[int], idx: int):
            if idx == len(nums):
                if curlist not in res:
                    res.append(curlist)
                return

            search(curlist + [nums[idx]], idx+1)
            search(curlist, idx+1)

        search([],0)
        return res

#%%
# DFS
class S2:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(depth: int, start: int, lst: List[int]):
            if lst not in res:
                res.append(lst)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                dfs(depth+1, i+1, lst+[nums[i]])
        
        dfs(0,0,[])
        return res
