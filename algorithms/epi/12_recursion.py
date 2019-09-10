#%% [markdown]
'''
Recursion is an approach to problem solving where the solution depends partially on solutions to smaller instances of related problems.

A recursive function consists of base cases and calls to the same function with different arguments.
- Identifying the base cases
- Ensuring progress

backtracking and branch-bound are naturally formulated using recursion.

### Tips
- Recursion is especially suitable when the input is expressed using recursive rules such as computer grammar.
- Recursion is a good choice for search, enumeration and divide-and-conquer.
- Use recursion as alternative to deeply nested iteration loops.
- If you are asked to remove recursion from a program, consider mimicking call stack with the stack data structure.
- If a recursive function may end up being called with the same arguments more than once, cache the results.

'''

#%%
# Calculating the greatest common divisor (GCD) of two numbers
# The central idea is that if y > x, the GCD of x and y is the GCD of x and y-x.
# By extension, this implies that the GCD of x and y is the GCD of x and y mod x.

def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)

# Time complexity O(log max(x,y)), space complexity O(n), n is the maximum depth of the function call stack.
# When converting to one which loops, space complexity O(1).

#%% [markdown]
'''
### Variant
Triomino placement
A triomino is formed by joining three unit-sized squares in an L-shape.
A triomino placement for an n*n Mboard with the top-left square misssing.
Divide-and-conquer

Generate the power set
The power set of a set S is the set of all subsets of S, including both the empty set and S itself.
Write a function that takes as input a set and returns its power set.
Hint: There are 2^n subsets for a given set S of size n. There are 2^k k-bit words.

'''


#%%
# Generate the power set

def generate_power_set(input_set):
    
    def directed_power_set(to_be_selected, selected_so_far):
        if to_be_selected == len(input_set):
            power_set.append(list(selected_so_far))
            return

        directed_power_set(to_be_selected+1, selected_so_far)
        directed_power_set(to_be_selected+1, selected_so_far + [input_set[to_be_selected]])


    power_set = []
    directed_power_set(0, [])
    return power_set

# C(n) = 2C(n-1)
# Time complexity O(n2^n)

#%%
# Generate the power set

import math

def generate_power_set(S):
    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set
    

#%%
