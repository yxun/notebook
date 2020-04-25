#%%
from nose.tools import assert_equal


#%% [markdown]
'''
- Median of Two Sorted Arrays
- https://leetcode.com/problems/median-of-two-sorted-arrays/
- Hard
'''

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

#%% [markdown]
'''
### Divide and conquer
- if x[n/2] == y[n/2]: return
- if x[n/2] < y[n/2]: find in x[n/2...n] and y[1...n/2]
- else find in x[1...n/2] and y[n/2...n]
### Other considerations
- if length of x and y are different
- if (len(x) + len(y)) % 2 == 0
'''

#%%
from math import floor

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, floor(n/2) + 1)
        else:
            smaller = self.findKth(nums1, nums2, floor(n/2))
            bigger = self.findKth(nums1, nums2, floor(n/2) + 1)
            return (smaller + bigger) / 2.0


    def findKth(self, A, B, k):

        if len(A) == 0:
            return B[k-1]
        if len(B) == 0:
            return A[k-1]
        if k == 1:
            return min(A[0], B[0])
        
        a = A[floor(k/2) - 1] if len(A) >= k/2 else None
        b = B[floor(k/2) - 1] if len(B) >= k/2 else None
        if b is None or (a is not None and a < b):
            return self.findKth(A[floor(k/2):], B, k - floor(k/2))
        return self.findKth(A, B[floor(k/2):], k - floor(k/2))



#%%
s = Solution()
nums1 = [1, 3]
nums2 = [2]
expected = 2.0
assert_equal(s.findMedianSortedArrays(nums1, nums2), expected)

nums1 = [1, 2]
nums2 = [3, 4]
expected = 2.5
assert_equal(s.findMedianSortedArrays(nums1, nums2), expected)
print("Success")

#%%
