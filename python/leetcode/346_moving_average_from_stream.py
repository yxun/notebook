#%%
"""
- Moving Average from Data Stream
- https://leetcode.com/problems/moving-average-from-data-stream/
- Easy
"""

#%%
"""
Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
"""

#%%
##
class MovingAverage:
    def __init__(self, size):
        """
        :type size: int
        """
        self.size = size
        self.curSize = 0
        self.buffer = []

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.curSize < self.size:
            self.buffer.append(val)
            self.curSize += 1
            return sum(self.buffer) / self.curSize
        else:
            self.buffer.pop(0)
            self.buffer.append(val)
            return sum(self.buffer) / self.size


#%%
from collections import deque

class MovingAverage:
    def __init__(self, size):
        """
        :type size: int
        """
        self.buffer = deque(maxlen=size)

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.buffer.append(val)
        return sum(self.buffer) / len(self.buffer)
        