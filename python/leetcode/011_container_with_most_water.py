#%% [markdown]
"""
- 11. Container With Most Water
- https://leetcode.com/problems/container-with-most-water/
- Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


#%%
# S(i,j) = min(ai,aj) * (j-i)
# Move two endpoints 
# when a(left) < a(right), For j < right, S(left, right) > S(left, j)
# So when a(left) < a(right), move left forward. Same when a(left) > a(right), move right backward

class S1:

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        left, right = 0, n-1
        most_water = 0
        while left <= right:
            water = (right - left) * min(height[left], height[right])
            most_water = max(water, most_water)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return most_water


#%%
from nose.tools import assert_equal

s = S1()
height = [1,8,6,2,5,4,8,3,7]
expected = 49

assert_equal(s.maxArea(height), expected)
print('Success')


#%%
