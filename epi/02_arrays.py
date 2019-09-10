#%% [markdown]
'''
Retrieving and updating A`[i]` takes O(1) time

When working with arrays you should take advantage of the fact that you operate efficiently on both ends
'''


#%%
# reorder an array in place so that the even entries appear first

def even_odd(A):
    next_even, next_odd = 0, len(A) -1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1


#%% [markdown]
'''
- Array problems often have simple brute-force solutions that use O(n) space, but there are subtler solutions that use the array itself to reduce space complexity
- Filling an array from the front is slow, so see if it's possible to write values from the back
- Instead of deleting an entry, consider overwriting it
- When dealing with integers encoded by an array consider processing the digits from the back of the array. Alternately, reverse the array so the least-significant digit is the first entry
- Be comfortable with writing code that operates on subarrays
- Avoid off-by-1 errors -- reading past the last element of an array
- Don't worry about preserving the integrity of the array (sortedness, keeping equal entries together, etc.) until it is time to return
- An array can serve as a good data structure when you know the distribution of the elements in advance
- When operating on 2D arrays, use parallel logic for rows and for columns
'''

'''
Arrays in Python are provided by the list type. The tuple type with the constraint that it is immutable.

The key property of a list is that it is dynamically-resized.
- Know the syntax for instantiating a list, e.g. `[1,2,3]`, `[1]` + `[2]` * 10, list(range(100)), List comprehension
- The basic operations are len(A), A.append(42), A.remove(2), and A.insert(3, 28)
- Know how to instantiate a 2D array
- Checking if a value is present in an array is as simple as a in A (O(n) time)
- Understand how copy works, i.e. the difference between B = A and B = list(A)
- Understand what a deep copy is, and how it differs from a shallow copy, i.e. how copy.copy(A) differs from copy.deepcopy(A)
- Key methods for list include: 
    - min(A), max(A), 
    - binary search for sorted lists (bisect.bisect(A, 6), bisect.bisect_left(A, 6) and bisect.bisect_right(A, 6))
    - A.reverse() (in-place), reversed(A) (returns an iterator)
    - A.sort() (in-place), sorted(A) (returns a copy)
    - del A`[i]` (delete the i-th element), and del A`[i:j]` (removes the slice)
- Slicing is a very succinct way of manipulating arrays. A[::-1] rotates list, A[k:] + A[:k] rotates A by k to the left, B = A[:] does a (shallow) copy of A into B
- List comprehension is a succinct way to create lists. Sets and dictionaries also support list comprehensions.
'''

#%%
# Quick sort
# Complexity: best O(nlog(n)) avg O(nlog(n)) worst O(n^2)

def quick_sort(arr):
    arr = quick_sort_recur(arr, 0, len(arr)-1)
    return arr

def quick_sort_recur(arr, low, high):
    if low < high:
        part = partition(arr, low, high)
        # start two recrsive calls
        quick_sort_recur(arr, low, part-1)
        quick_sort_recur(arr, part+1, high)

    return arr

def partition(arr, low, high):
    part = low
    for pos in range(low, high):
        if arr[pos] < arr[high]:    # high is the pivot
            arr[pos], arr[part] = arr[part], arr[pos]
            part += 1
    
    arr[part], arr[high] = arr[high], arr[part]
    return part

#%%
nums = [2,6,8,5,1,4,9,3,7]
print(quick_sort(nums))

#%%
# Dutch Flag Partition
# Save space complexity sacrifice time complexity
# space complexity O(1), time complexity O(n^2)

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    for i in range(len(A)):
        # Look for a smaller element
        for j in range(i + 1, len(A)):
            if A[j] < pivot:
                A[i], A[j] = A[j], A[i]
                break
    # Second pass: group elements larger than pivot
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        # Look for a larger element. Stop when we reach an element less than
        # pivot, since first pass has moved them to the start of A
        for j in reversed(range(i)):
            if A[j] > pivot:
                A[i], A[j] = A[j], A[i]
                break

#%%
# Dutch Flag Partition
# time complexity O(n) space complexity O(1)

RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
    pivot = A[pivot_index]
    # First pass: group elements smaller than pivot
    smaller = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[i], A[smaller] = A[smaller], A[i]
            smaller += 1
    # Second pass: group elements larger than pivot
    larger = len(A) - 1
    for i in reversed(range(len(A))):
        if A[i] < pivot:
            break
        elif A[i] > pivot:
            A[i], A[larger] = A[larger], A[i]
            larger -= 1


#%% [markdown]
'''
### Variant
- Assuming that keys take one of three values, reorder the array so that all objects with the same key appear together
- Given an array A of n objects with keys that takes one of four values, reorder the array so that all objects that have the same key appear together
- Given an array A of n objects with Boolean-valued keys, reorder the array so that objects that have the key false appear first
- Given an array A of n objects with Boolean-valued keys, reorder the array so that objects that have the key false appear first. The relative ordering of objects with key true should not change
'''


#%%
