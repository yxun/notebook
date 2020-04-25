#%%
"""
- Design Hit Counter
- https://leetcode.com/problems/design-hit-counter/
- Medium
"""

#%%
"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 
Follow up:
What if the number of hits per second could be very large? Does your design scale?
"""

#%%

class HitCounter:

    def __init__(self):
        ...
        self.l = []

    def hit(self, timestamp):
        """
        :type timestamp: int
        :rtype: None
        """
        if len(self.l) == 0:
            self.l.append(timestamp)
        elif timestamp - self.l[0] < 300:
            self.l.append(timestamp)
        else:
            t = self.l.pop(0)
            while self.l and self.l[0] == t:
                self.l.pop(0)
            self.l.append(timestamp)

    def getHits(self, timestamp):
        """
        :type timestamp: int
        :rtype: int
        """
        if len(self.l) == 0: return 0

        for i in range(len(self.l)):
            if timestamp - self.l[i] >= 300:
                continue
            else:
                return len(self.l[i:])
        return 0
