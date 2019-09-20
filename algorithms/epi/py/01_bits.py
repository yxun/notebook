#%%
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

#%%
count_bits(12)

#%% [markdown]
'''
- Be very comfortable with the bitwise operators, particularly XOR
- Understand how to use masks and create them in an machine independent way
- Know fast ways to clear the lowermost set bit
- Understand signedness and its implications to shifting
- Consider using a cache to accelerate operations by using it to brute-force small inputs
- Be aware that commutativity and associativity can be used to perform operations in parallel and reorder operators
'''

#%% [markdown]
'''
### Key methods
- abs(-34.5)
- math.ceil(2.17)
- math.floor(3.14)
- min(1,2)
- max(1,2)
- pow(2.17, 3.14) # alternately, 2.17 ** 3.14
- math.isclose(2.17, 3.14)

- random.randrange(28)
- random.randint(8, 16)
- random.random()
- random.shuffle([1,2,3])
- random.choice([1,2,3])

### Interconvert integers and strings
- str(42)
- int('42')
- str(3.14)
- float('3.14')
- float('inf')
- float('-inf')
'''

#%% [markdown]
'''
### Computing the parity of a word
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0.
'''


#%%
# brute-force
def parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result


#%%
# erase the lowest set bit in a word
# lowest set bit y = x & ~(x-1)
def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x-1   # Drops the lowest set bit of x
    return result


#%% [markdown]
'''
### Two keys to performance
- Processing multiple bits at a time
- Caching results in an array-based lookup table

### Variant
- Right propagate the rightmost set bit in x, e.g. turns01010000 to 01011111
- Compute x modulo a power of two, e.g. returns 13 for 77 mod 64
- Test if x is a power of 2
'''


#%%
