#%%
"""
- Combination Sum II
- https://leetcode.com/problems/combination-sum-ii/
- Medium

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

#%%
# three differences from combination sum i
# - Don't need set candidates
# - recursion using i + 1 instead of i
# - check if combo not in res , then append combo into res
class S:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(remain, combo, index):
            if remain == 0 and combo not in res:
                res.append(combo)
                return
            for i in range(index, len(candidates)):
                if candidates[i] > remain:
                    break
                dfs(remain-candidates[i], combo+[candidates[i]], i+1)

        candidates.sort()
        res = []
        dfs(target, [], 0)
        return res

#%%
