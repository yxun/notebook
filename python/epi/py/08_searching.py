#%% [markdown]
'''
This chapter focus is on static data stored in sorted order in an array.

### Binary search
The idea is to eliminate half the keys from consideration by keeping the keys in sorted order.
Search O(logn). Sort O(nlogn).

'''


#%%
# An iterative implementation of Binary search

def bsearch(t, A):
    low, high = 0, len(A)-1
    while low <= high:
        mid = low + (high-low)//2     # (L+U)//2 can potentially lead to overflow
        if A[mid] < t:
            low = mid + 1
        elif A[mid] == t:
            return mid
        else:
            high = mid - 1
    return -1


#%%
# An recursive implementation of Binary search

def bsearch_recursive(A, low, high, t):
    
    # Check base case
    if high >= 1:
        mid = low + (high-low)//2

        if A[mid] == t:
            return mid
        elif A[mid] < t:
            return bsearch_recursive(A, mid+1, high, t)
        else:
            return bsearch_recursive(A, low, mid-1, t)
    else:
        return -1

#%%
# using library
# Time complexity O(logn)

import bisect
import collections

Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student):
    return (-student.grade_point_average, student.name)     # higher GPA comes first, with ties broken on name.

def search_student(students, target, comp_gpa):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

#%% [markdown]
'''
### Tips
- Binary search is applicable to more than just searching in sorted arrays, e.g., it can be used to search an interval of real numbers or integers.
- If your computation performed after sorting is faster than sorting, e.g., O(n) or O(logn), look for solutions that do not perform a complete sort.
- Consider time/space tradeoffs, such as making multiple passes through the data.
'''

'''
### Know searching libraries
The bisect module provides binary search functions for sorted list.
- bisect.bisect_left(a, x): To find the first element that is greater than or equal to a target value x.
This call returns the index of the first entry that is greater than or equal to the targeted value.
- bisect.bisect_right(a, x): To find the first element that is greater than a targeted value x.
This call returns the index of the first entry that is greater than the targeted value x. 
If all elements in the list are less than or equal to x, the returned value is len(a).
'''

#%%
# Search a sorted array with repeated elements for first occurrence of k
# Hint: What happens when every entry equals k ? Don't stop when you first see k.

# If we see the element at index i equals k, although we do not know whether i is the first element equal to k,
# we do know that no subsequent elements can be the first one. Therefore we remove all elements with index i+1 or more.

# Time complexity O(logn)

def search_first_of_k(A, k):
    left, right, result = 0, len(A)-1, -1
    # A[left:right+1] is the candidate set.
    while left <= right:
        mid = left + (right-left)//2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] == k:
            result = mid
            right = mid - 1     # Nothing to the right of mid can be solution
        else:   # A[mid] < k
            left = mid + 1
    return result

#%% [markdown]
'''
### Variant
- Design an efficient algorithm that takes a sorted array and a key, and finds the index of the first occurrence of an element greater than that key.
- Let A be an unsorted array of n integers, with A[0] >= A[1] and A[n-2] <= A[n-1].
Call an index i a local minimum if A[i] is less than or equal to its neighbors. How would you efficiently find a local minimum, if one exists?
- Write a program which takes a sorted array A of integers, and an integer k, and returns the interval enclosing k,
i.e., the pair of integers L and U such that L is the first occurrence of k in A and U is the last occurrence of k in A.
If k does not appear in A, return [-1,-1].
For example if A = <1,2,2,4,4,4,7,11,11,13> and k=11, you should return [7,8]
- Write a program which tests if p is a prefix of a string in an array of sorted strings.
'''


#%%
