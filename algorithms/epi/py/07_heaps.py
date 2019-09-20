#%% [markdown]
'''
A heap is a specialized binary tree. It is a complete binary tree.
The keys must satisfy the heap property: the key at each node is at least as great as the keys stored at its children.
A max-heap can be implemented as an array; the children of the node at index i are at indices 2i+1 and 2i+2.
A heap is sometimes referred to as a priority queue. Each element has a "priority" associated with it, and deletion removes the element with the highest priority.

'''

'''
### max element 
- insertions: O(logn)
- lookup: O(1)
- deletion: O(logn)

The extract-max operation is defined to delete and return the max element.
Searching for arbitrary keys has O(n) time complexity.
The min-heap supports O(1) time lookups for the minimum element.

'''


#%%
# Take a sequence of strings and cannot back up to read an eariler value.
# Return the k longest strings in the sequence.

# Time complexity O(nlogk)
# We could improve best-case time by comparing the new string's length with the length of the string at the top of the heap.

import itertools, heapq

def top_k(k, stream):
    # Entries are compared by their lengths.
    min_heap = [(len(s), s) for s in itertools.islice(stream, k)]
    heapq.heapify(min_heap)
    for next_string in stream:
        # Push next_string and pop the shortest string in min_heap.
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    return [p[1] for p in heapq.nsmallest(k, min_heap)]


#%% [markdown]
'''
### Tips
Use a heap when all you care about is the largest or smallest elements.
A heap is a good choice when you need to compute the k largest or k smallest elements.
'''

'''
### Know heap libraries
heapq module
- heapq.heapify(L), transforms the elements in L into a heap in-place.
- heapq.nlargest(k, L), heapq.nsmallest(k, L)
- heapq.heappush(h, e)
- heapq.heappop(h)
- heapq.heappushpop(h, a)
- e = `h[0]`, returns the smallest element on the heap without popping it.

heapq only provides min-heap functionality.
If you need to build a max-heap on integers or floats, insert their negative to get the effect of a max-heap.
For objects, implement __lt()__ appropriately.
'''


#%%
# Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.
# For example, if the input is <3,5,7>, <0,6>, and <0,6,28>,
# then the output is <0,0,3,5,6,6,7,28>

# A brute-force approach: concatenate these sequences and then sort it. Time complexity O(nlogn).

# A better approach using min-heap for maintaining a collection of elements.
# k the number of input sequences. Time complexity O(nlogk). Space complexity O(k).

import heapq

def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    # Builds a list of iterators for each array in sorted_arrays.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]

    # Puts first element from each iterator in min_heap.
    for i, it in enumerate(sorted_arrays_iters):
        first_element = next(it, None)
        if first_element is not None:
            heapq.heappush(min_heap, (first_element, i))

    result = []
    while min_heap:
        smallest_entry, smallest_array_i = heapq.heappop(min_heap)
        smallest_array_iter = sorted_arrays_iters[smallest_array_i]
        result.append(smallest_entry)
        next_element = next(smallest_array_iter, None)
        if next_element is not None:
            heapq.heappush(min_heap, (next_element, smallest_array_i))
    return result


# Pythonic solution
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))


#%%
