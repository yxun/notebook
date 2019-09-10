#%%
# Making changes for US currency, wherein coins 1, 5, 10, 25, 50, 100 cents
# Greedy algorithm once it selects , it never changes that selection.

def change_making(cents):
    COINS = [100, 50, 25, 10, 5, 1]
    num_coins = 0
    for coin in COINS:
        num_coins += cents / coin
        cents %= coin
    return num_coins


#%% [markdown]
'''
### Tips
- A greedy algorithm is often the right choice for an optimization problem where there's a natural set of choices to select from.
- It's often easier to conceptualize a greedy algorithm recursively, and then implement it using iteration for higher performance.
- Even if the greedy approach does not yield an optimum solution, it can give insights into the optimum algorithm.
- Sometimes the correct greedy algorithm is not obvious.
'''


#%%
# Write a program that takes as input a sorted array and a given target value and determines if there are two entries in the array that add up to that value.
# Use a hash table, time complexity O(n), space complexity O(n)

# Use invariants, shrink the subarray from one side or the other.
# An invariant is a condition that is true during execution of a program.

def has_two_sum(A, t):
    i, j = 0, len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False

# Time complexity O(n), space complexity O(1)


#%%
# The 3-sum problem
# Input an array and a number, and determines if there are three entries in the array (not necessarily distinct) which add up to the specified number.

def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t-a) for a in A)

# Time complexity O(n^2), space complexity O(1)

# Variant
# Solve the same problem when the three elements must be distinct.

#%%
