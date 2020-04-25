#%%
"""
- LRU Cache
- https://leetcode.com/problems/lru-cache/
- Medium

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

"""

#%%
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.keyVals = OrderedDict()
        
    def get(self, key):
        if key in self.keyVals:
            value = self.keyVals[key]
            self.keyVals.move_to_end(key)
            return value
        else:
            return -1
        
    def push(self, key, value):
        if key in self.keyVals:
            self.keyVals[key] = value
            self.keyVals.move_to_end(key)
        elif len(self.keyVals) == self.capacity:
            oldest = next(iter(self.keyVals))
            del self.keyVals[oldest]
        self.keyVals[key] = value
         