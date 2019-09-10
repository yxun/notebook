#%% [markdown]
'''
Stacks: LIFO, Queues: FIFO

### Stacks
Supports two basic operations: push and pop. 
Time complexity O(1)
Additional operations: peek

Useful for creating reverse iterators for sequences.
'''


#%%
# print the entries of a singly-linked list in reverse order
# Time and space complexity O(n)

def print_linked_list_in_reverse(head):
    nodes = []
    while head:
        nodes.append(head.data)
        head = head.next
    while nodes:
        print(nodes.pop())


#%% [markdown]
'''
### Know stack libraries
Some of the problems require you to implement your own stack class; for others, use the built-in list-type
- s.append(e) push
- `s[-1]` peek
- s.pop() pop
- len(s) == 0 tests if the stack is empty

'''


#%%
# Implement a stack includes a max operation
# The max method should return the maximum value stored in the stack

# The simplest way by iterating through the underlying array. The time complexity O(n), space complexity O(1)
# The time complexity can be reduced to O(logn) using a heap or a BST and a hash table. The space complexity increases to O(n)

# Improve on the time complexity of popping by caching, trading time for space.
# Time complexity O(1), space complexity O(n)

import collections

class Stack:
    ElementWithCachedMax = collections.namedtuple('ElementWithCachedMax', ('element', 'max'))

    def __init__(self):
        self._element_with_cached_max = []

    def empty(self):
        return len(self._element_with_cached_max) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._element_with_cached_max[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self._element_with_cached_max.pop().element

    def push(self, x):
        self._element_with_cached_max.append(
            self.ElementWithCachedMax(x, x if self.empty() else max(x, self.max()))
        )


#%%
# Improve on the best-case space needed

class Stack:

    class MaxWithCount:

        def __init__(self, max, count):
            self.max, self.count = max, count

    
    def __init__(self):
        self._element = []
        self._cached_max_with_count = []

    def empty(self):
        return len(self._element) == 0

    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return self._cached_max_with_count[-1].max

    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        pop_element = self._element.pop()
        current_max = self._cached_max_with_count[-1].max
        if pop_element == current_max:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return pop_element

    def push(self, x):
        self._element.append(x)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(x, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if x == current_max:
                self._cached_max_with_count[-1].count += 1
            elif x > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(x, 1))


#%% [markdown]
'''
### Queues
Supports two operations: enqueue and dequeue.
A queue can be implemented using a linked list, time complexity O(1)
A deque, a double-ended queue, is a doubly linked list. 
An insertion to the front called a push, and an insertion to the back called an inject.
A deletion from the front called a pop, and a deletion from the back called an eject.
'''


#%%
# Implement enqueue, dequeue and a max method
# Time complexity of enqueue and dequeue O(1). Time complexity of max O(n)

class Queue:

    def __init__(self):
        self._data = []

    def enqueue(self, x):
        self._data.append(x)

    def dequeue(self):
        return self._data.pop(0)

    def max(self):
        return max(self._data)

#%% [markdown]
'''
### Know queue libraries
Some of the problems require you to implement your own queue class; for others, use the collections.deque class.
- q.append(e) push
- `q[0]` retrieve, but not remove the element at the front of the queue; `q[-1]` retrieve, but not remove, the element at the back of the queue
- q.popleft() remove and return the element at the front of the queue

'''


#%%
# Computing binary tree nodes in order of increasing depth
# Time complexity O(n), space complexity O(m), where m is the maximum number of nodes at any single depth

import collections

def binary_tree_depth_order(tree):
    result, curr_depth_nodes = [], collections.deque([tree])
    while curr_depth_nodes:
        next_depth_nodes, this_level = collections.deque([]), []
        while curr_depth_nodes:
            curr = curr_depth_nodes.popleft()
            if curr:
                this_level.append(curr.data)
                # Defer the null checks to the null test above.
                next_depth_nodes += [curr.left, curr.right]

        if this_level:
            result.append(this_level)
        curr_depth_nodes = next_depth_nodes
    return result


#%% [markdown]
'''
### Variant
- Write a program which takes as input a binary tree and returns the keys in top down, alternating left-to-right and right-to-left order, starting from left-to-right.
- Write a program which takes as input a binary tree and returns the keys in botton up, left-to-right order.
- Write a program which takes as input a binary tree with integer keys, and returns the average of the keys at each level.
'''


#%%
