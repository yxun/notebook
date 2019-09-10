#%% [markdown]
'''
heapsort is in-place but not stable; merge sort is stable but not in-place; quicksort runs O(n^2) time in worst-case.
An in-place sort is one which uses O(1) space
A stable sort is one where entries which are equal appear in their original order.

### Tips
- Sorting problems come in two flavors: 
1. use sorting to make subsequent steps simpler.
2. design a custom sorting routine.
- If the inputs have a natural ordering, and sorting can be used as a preprocessing step to speed up searching.

### Know sorting libraries
To sort a list in-place, use the sort() method; to sort an iterable, use the function sorted().

'''


#%%
# Compute the intersection of two sorted arrays
# result should not include duplicates

# Time complexity O(mlogn)
# good solution if one array is much smaller than the other. 

def intersect_two_sorted_arrays(A, B):
    def is_present(k):
        i = bisect.bisect_left(B, k)
        return i < len(B) and B[i] == k

    return [
        a for i, a in enumerate(A) if (i == 0 or a != A[i-1]) and is_present(a)
    ]

# If both array lengths are similar, we can achieve linear runtime by simultaneously advancing through the two input arrays in increasing order.
# Time complexity O(m+n)

def intersect_two_sorted_arrays(A, B):
    i, j, intersection_A_B = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                intersection_A_B.append(A[i])
            i, j = i+1, j+1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection_A_B
    
#%%
# Render a calendar
# Write a program that takes a set of events, and determines the maximum number of events that take place concurrently.
# Time complexity O(nlogn), space complexity O(n)

import collections

# Event is a tuple (start_time, end_time)
Event = collections.namedtuple('Event', ('start', 'finish'))

# Endpoint is a tuple (start_time, 0) or (end_time, 1) so that if times
# are equal, start_time comes first
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def find_max_simultaneous_events(A):
    # Builds an array of all endpoints.
    E = ([Endpoint(event.start, True) for event in A] + [Endpoint(event.finish, False) for event in A])
    # Sorts the endpoint array according to the time, breaking ties by putting
    # start times before end times.
    E.sort(key=lambda e: (e.time, not e.is_start))

    # Track the number of simultaneous events, record the maximum number of 
    # simultaneous events.
    max_num_simultaneous_events, num_simultaneous_events = 0, 0
    for e in E:
        if e.is_start:
            num_simultaneous_events += 1
            max_num_simultaneous_events = max(num_simultaneous_events, max_num_simultaneous_events)
        else:
            num_simultaneous_events -= 1
        
    return max_num_simultaneous_events

# Variant
# Users 1,2,...,n share an Internet connection. User i uses bi bandwidth from time si to fi, inclusive. What is the peak bandwidth usage?

#%%
