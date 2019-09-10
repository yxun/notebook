#%% [markdown]
'''
DP is a general technique for solving optimization, search, and counting problems that can be decomposed into subproblems.
Like divide-and-conquer, DP solves the problem by combining the solutions of multiple smaller problems, but what makes DP different is that the same subproblem may reoccur.
Therefore, a key to making DP efficient is caching the results of intermediate computations.


'''


#%%
# fibonacci
# F(n) = F(n-1) + F(n-2), with F(0) = 0, F(1) = 1
# compute F(n) recursively without caching, time complexity is exponential in n.

# Caching intermediate results , time complexity linear in n, albeit at the expense of O(n) storage.

def fibonacci(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


#%%
# fibonacci, O(n) time and O(1) space

def fibonacci(n):
    if n <= 1:
        return n

    f_minus_2, f_minus_1 = 0, 1
    for _ in range(1, n):
        f = f_minus_2 + f_minus_1
        f_minus_2, f_minus_1 = f_minus_1, f
    return f_minus_1


#%% [markdown]
'''
The key to solving a DP problem efficiently is finding a way to break the problem into subproblems
- the original problem can be solved relatively easily once solutions to the subproblems are available, and
- these subproblem solutions are cached.
'''

'''
### Tips
- Consider using DP whenever you have to make choices to arrive at the solution.
When you can construct a solution to the given instance from solutions to subinstances of smaller problems of the same kind.
- Counting and decision problems. 
where you can express a solution recursively in terms of the same computation on smaller instances.
- For efficiency the cache is built "bottom-up",i.e.,iteratively.
- When DP is implemented recursively the cache is typically a dynamic data structure such as a hash table or a BST
When it is implemented iteratively the cache is usually a one- or multi- dimensional array.
- To save space, cache space may be recycled once it is known that a set of entries will not be looked up again.
- DP is based on combining solutions to subproblems to yield a solution to the original problem.

'''


#%%
# find the maximum sum over all subarrays of a given array of integer.

import itertools

def find_maximum_subarray(A):
    min_sum = max_sum = 0
    for running_sum in itertools.accumulate(A):
        min_sum = min(min_sum, running_sum)
        max_sum = max(max_sum, running_sum - min_sum)
    return max_sum


#%%
# Count the number of ways to traverse a 2D Array
# Write a program that counts how many ways you can go from the top-left to the bottom-right in a 2D array.
# All moves must either go right or down.

def number_of_ways(n, m):
    def compute_number_of_ways_to_xy(x, y):
        if x == y == 0:
            return 1

        if number_of_ways[x][y] == 0:
            ways_top = 0 if x == 0 else compute_number_of_ways_to_xy(x-1, y)
            ways_left = 0 if y == 0 else compute_number_of_ways_to_xy(x, y-1)
            number_of_ways[x][y] = ways_top + ways_left
        return number_of_ways[x][y]

    number_of_ways = [[0] * m for _ in range(n)]
    return compute_number_of_ways_to_xy(n-1, m-1)

# Time complexity O(nm), space complexity O(nm)
# Variant: Solve the same problem using O(min(n,m)) space
# Variant: Solve the same problem in the presence of obstacles, spcified by a Boolean 2D array.
