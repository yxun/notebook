#%% [markdown]
'''
A hash table is a data structure used to store keys, optionally, with corresponding values.
Inserts, deletes and lookups run in O(1 + n/m) time on average. n is the number of objects and m is the length of the array. 
The underlying idea is to store keys in an array. A key is stored in the array locations ("slots") based on its "hash code".
The hash code is an integer computed from the key by a hash function.

If two keys map to the same location, a "collision" occur. The standard mechanism to deal with collistions is to maintain a linked list.
A hash function has one hard requirement, equal keys should have equal hash coded.

A common mistake with hash tables is that a key that's present in a hash table will be updated.
If you have to update a key, first remove it, then update it, and finally, add it back.
As a rule, you should avoid using mutable objects as keys.

A hash table is a good data structure to represent a dictionary, i.e., a set of strings.
In some applications, a trie, is used to store a dynamic set of strings.

'''


#%%
# example of a hash function suitable for strings

import functools

def string_hash(s, modulus):
    MULT = 997
    return functools.reduce(lambda v, c: (v * MULT + ord(c)) % modulus, s, 0)


#%%

# Anagrams, rearranging letters of one set of words, you get another set of words.
# Two words are anagrams if and only if they result in equal strings after sorting.
# Add sort(s) for each string s in the dictionary to a hash table.
# The sorted strings are keys, and the values are arrays of the corresponding strings.
# Time complexity O(nmlogm) , m length of the strings

import collections

def find_anagrams(dictionary):
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        # Sorts the string, uses it as a key, and then appends the original
        # string as another value into hash table.
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)

    return [
        group for group in sorted_string_to_anagrams.values() if len(group) >= 2
    ]


#%%
# Design of a hashable class
# The time complexity of computing the hash is O(n), where n is the number of strings in the contact list.
# Hash codes are often cached for performance, with the caveat that the cache must be cleared if objects fields that are referenced by the hash function are updated.

class ContactList:

    def __init__(self, names):
        '''
        names is a list of strings.
        '''
        self.names = names

    def __hash__(self):
        # Conceptually we want to hash the set of names. Since the set type is
        # mutable, it cannot be hashed. Therefore we use frozenset.
        return hash(frozenset(self.names))

    def __eq__(self, other):
        return set(self.names) == set(others.names)


def merge_contact_lists(contacts):
    '''
    contacts is a list of ContactList.
    '''
    return list(set(contacts))


#%% [markdown]
'''
### Tips
- Hash tables have the best theoretical and real-world performance for lookup, insert and delete.
- Consider using a hash code as a signature to enhance performance
- Consider using a precomputed lookup table, e.g., from character to value, or character to character.
- Understand the relationship between logical equality and the fields the hash function must inspect.
- Sometimes you'll need a multimap, i.e., a map that contains multiple values for a single key, or a bi-directional map.
'''

'''
### Know hash table libraries
- set, dict, collections.defaultdict, and collections.Counter
set stores keys, whereas the others store key-value pairs.
dict returns a KeyError exception when a key is not present. collections.defaultdict returns the default value of the type.
collections.Counter is used for counting the number of occurrences of keys with set-like operations.
- Important operations for set: s.add(), s.remove(), s.discard(), x in s, s <= t (is s a subset of t), and s - t (elements in s that are not in t).
- Iteration over a key-value collection yields the keys. To iterate over the key-value pairs, iterate over items(); to iterate over values, use values().
- Mutable containers are not hashable.
- The built-in hash() function can simplify the implementation of a hash function for a user-defined class,i.e., implementing __hash__(self)

'''


#%%
# Is letter constructible
# Time complexity O(m+n), space complexity O(L)

import collections

def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # Compute the frequencies for all chars in letter_text.
    char_frequency_for_letter = collections.Counter(letter_text)

    # Checks if characters in magazine_text can cover characters in
    # char_frequency_for_letter.
    for c in magazine_text:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
                if not char_frequency_for_letter:
                    # All characters for letter_text are matched
                    return True

    return not char_frequency_for_letter


# Pythonic solution. 
# The subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return (not collections.Counter(letter_text) - collections.Counter(magazine_text))
    

#%%
