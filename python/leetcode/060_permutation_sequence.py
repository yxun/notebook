#%%
"""
- Permutation Sequence
- https://leetcode.com/problems/permutation-sequence/
- Medium

The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
"""

#%%
# find one digit and then + rest of the n-1 digits permutation
import math

class S:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        seq, k, fact = '', k-1, math.factorial(n-1)
        perm = [ i for i in range(1, n+1) ]
        for i in reversed(range(n)):
            curr = perm[k//fact]
            seq += str(curr)
            perm.remove(curr)
            if i > 0:
                k %= fact
                fact //= i
        
        return seq

#%%