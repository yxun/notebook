#%%
"""
- Beautiful Arrangement
- https://leetcode.com/problems/beautiful-arrangement/
- Medium

Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
 

Now given N, how many beautiful arrangements can you construct?

Example 1:

Input: 2
Output: 2
Explanation: 

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
 

Note:

N is a positive integer and will not exceed 15.
"""

#%%
# X is the set of still available numbers
class S1:
    def countArragement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def count(i, X):
            if i == 1:
                return 1
            return sum(count(i-1, X- {x}) for x in X if x%i == 0 or i%x == 0)
        
        return count(N, set(range(1, N+1)))
        