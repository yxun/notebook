#%%
"""
- Largest Rectangle in Histogram
- https://leetcode.com/problems/largest-rectangle-in-histogram/
- Hard

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""

#%%
class S:
    def largestRectangleArea(self, heights):
        """
        :type: heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        result = 0
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                result = max(result, h*w)
            stack.append(i)
        heights.pop()
        return result
        