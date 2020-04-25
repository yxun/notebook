#%%
"""
- Maximum XOR of Two Numbers in an Array
- https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
- Medium

Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:

Input: [3, 10, 5, 25, 2, 8]

Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
"""

#%%
class S:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0
        for i in range(32)[::-1]:
            answer <<= 1
            prefixes = {num >> i for num in nums}
            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)     # a^b^a = b, answer^1 equivalent answer + 1
        return answer
