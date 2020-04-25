#%%
"""
- Combinations
- https://leetcode.com/problems/combinations/
- Medium

Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

#%%
class S1:
    def combine(self, n, k):
        import itertools
        return [list(i) for i in itertools.combinations(range(1, n+1), k)]
        

#%%
class S2:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k == 1:
            return [[i+1] for i in range(n)]
        result = []
        if n > k:
            result = [r + [n] for r in self.combine(n-1, k-1)] + self.combine(n-1, k)
        elif n == k:
            # result = [r + [n] for r in self.combine(n-1, k-1)]
            result = [list(range(1, k+1))]
        return result
