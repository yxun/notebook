#%% [markdown]
'''
Inserting and deleting elements time complexity O(1). obtaining the kth element O(n)

Two types of linked list related problems:
- Implement your own list
- Exploit the standard list library
'''


#%%

class ListNode:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


#%%
# Implement a basic list API, search, insert, delete

def search_list(L, key):
    while L and L.data != key:
        L = L.next

    # If key was not present in the list, L will have become null
    return L

def insert_after(node, new_node):
    # insert new_node after node
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    # delete the node past this one. Assume node is not a tail
    node.next = node.next.next

#%% [markdown]
'''
### Tips
- Often have a simple brute-force solution that uses O(n) space, but a subtler solution that uses the existing list nodes to reduce space complexity to O(1)
- Very often, a problem on lists is conceptually simple, and is more about cleanly coding what's specified
- Consider using a dummy head to avoid having to check for empty lists
- It's easy to forget to update next ( and previous for double linked list) for the head and tail
- On singly linked list, benefit from using two iterators, one ahead of the other, or one advancing quicker than the other
'''

#%%
# Test for cyclicity

# Use two iterators to find if there is a cycle. In each iteration, advance the slow iterator by one and the fast iterator by two
# Use another two iterators to find the start of the cycle. By calculating the cycle length C. one iterator is C ahead of the other.

def has_cycle(head):
    def cycle_len(end):
        start, step = end, 0
        while True:
            step += 1
            start = start.next
            if start is end:
                return step
    
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            # Finds the start of the cycle
            cycle_len_advanced_iter = head
            for _ in range(cycle_len(slow)):
                cycle_len_advanced_iter = cycle_len_advanced_iter.next

            it = head
            # Both iterators advance in tandem
            while it is not cycle_len_advanced_iter:
                it = it.next
                cycle_len_advanced_iter = cycle_len_advanced_iter.next
            return it   # it is the start of cycle

    return None     # No cycle
