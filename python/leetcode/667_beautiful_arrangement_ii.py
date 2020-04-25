#%%
"""
- Beautiful Arrangement II
- https://leetcode.com/problems/beautiful-arrangement-ii/
- Medium

Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to n and obeys the following requirement: 
Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has exactly k distinct integers.

If there are multiple answers, print any of them.

Example 1:

Input: n = 3, k = 1
Output: [1, 2, 3]
Explanation: The [1, 2, 3] has three different positive integers ranging from 1 to 3, and the [1, 1] has exactly 1 distinct integer: 1.
Example 2:

Input: n = 3, k = 2
Output: [1, 3, 2]
Explanation: The [1, 3, 2] has three different positive integers ranging from 1 to 3, and the [2, 1] has exactly 2 distinct integers: 1 and 2.
Note:

The n and k are in the range 1 <= k < n <= 104.
"""

#%%
class S1:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        a = list(range(1, n+1))
        for i in range(1, k):
            a[i:] = a[:i-1:-1]
        return a


#%%
class S2:
    def constructArray(self, n, k):
        res = [1]
        sign = 1
        diff = k
        for _ in range(k):
            res.append(res[-1] + sign*diff)
            diff -= 1
            sign *= -1
        res += [i for i in range(1+k+1, n+1)]
        return res

#%%
# two pointers
class S3:
    def constructArray(self, n ,k):
        temp = [i for i in range(1, n+1)]
        l, r = 0, n-1
        res = []

        for i in range(k):
            if i % 2 == 0:
                res += [temp[l]]
                l += 1
            else:
                res += [temp[r]]
                r -= 1
        
        if k % 2 == 0:
            res += temp[l:r+1][::-1]
        else:
            res += temp[l:r+1]
        return res
