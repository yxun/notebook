#%% [markdown]
'''
A string can be viewed as a special kind of array. You should know how strings are represented in memory,
and understand basic operations on strings such as comparison, copying, joining, splitting, matching, etc.
Advanced string processing algorithms often use hash tables and dynamic programming.
'''

#%%
# time complexity O(n) and space complexity O(1)
def is_palindromic(s):
    # Note that s[~i] for i in [0, len(s)-1] is s[-(i+1)]
    return all(s[i] == s[~i] for i in range(len(s) // 2))

#%% [markdown]
'''
### string libraries
- key operators and functions: 
    - `s[3]`, len(s), s+t, `s[2:4]`, s in t, 
    - s.strip(), s.startswith(prefix), s.endswith(suffix),
    - 'Euclid,Axiom 5,Parallel Lines'.split(’,’)
    - 3 * '01', ','.join(('Gauss', 'Prince of Mathematicians', '1777-1855'))
    - s.tolower()
    - 'Name name, Rank rank'.format(name='Archimedes', rank=3)

### strings are immutable
This implies that concatenating a single character n times to a string in a for loop has O(n^2) time complexity
Some implementations of Python use tricks avoid having to do this allocation, reducing the complexity to O(n)

- Strings problems have simple brute-force solutions that use O(n) space, but subtler solutions to reduce space complexity to O(1)
- Understand the implications of a string type which is immutable
- Know alternatives to immutable strings, e.g. a list in Python
- Updating a mutable string from the front is slow, so see if possible to write values from the back
'''

#%%
# interconvert strings and integers

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # Adds the negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))


#%%
int_to_string(19876)

#%%
import functools
import string

def string_to_int(s):
    return functools.reduce(lambda running_sum, c: running_sum * 10 + string.digits.index(c),
                            s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)


#%%
string_to_int('76429')

#%%
# Base conversion
# The base b number system: a0*b^0 + a1*b^1 + a2*b^2 + ... + ak * b^k

# convert a string in base b1 to integer type (decimal number) using a sequence of multiply and adds
# and then convert that integer type to a string in base b2 using a sequence of modulus and division

import functools
import string

def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else 
                construct_from_base(num_as_int // base, base) + 
                string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else construct_from_base(num_as_int, b2))
    

#%%
print(convert_base('102', 3, 4))
print(convert_base('1A7', 13, 7))

#%%
