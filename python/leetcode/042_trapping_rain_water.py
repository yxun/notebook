#%%
"""
- Trapping Rain Water
- https://leetcode.com/problems/trapping-rain-water/
- Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

#%%
class S1:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r, water, min_height = 0, len(height)-1, 0, 0
        while l<r:
            min_height = min(height[l], height[r])
            while l<r and height[l] <= min_height:
                water += min_height - height[l]
                l += 1
            while l<r and height[r] <= min_height:
                water += min_height - height[r]
                r -= 1
        return water
        

#%%
###
class S2:
    def trap(self, height):
        if not height:
            return 0
        
        top_height = max(height)
        top_index = height.index(top_height)

        def subtrap(height):
            last_max = 0
            last = 0
            result = 0
            for h in height:
                if h < last_max:
                    result += last_max - h
                elif h > last_max:
                    last_max = h

            return result

        return subtrap(height[:top_index]) + subtrap(list(reversed(height[top_index+1:])))
