#%% [markdown]
'''
The stored values (the keys) are stored in a sorted order. Keys can be added to and deleted from a BST efficiently.
BST property: the key stored at a node is greater than or equal to the keys stored at the nodes of its left subtree
and less than or equal to the keys stored in the nodes of its right subtree.

A BST offers the ability to find the min and max elements, and find the next largest/next smallest element.

Key lookup, insertion, and deletion take time proportional to the height of the tree, in worst-case be O(n) if insertions and deletions are naively implemented.
Time complexity O(logn) for library implementations of BSTs. Both BSTs and hash tables use O(n) space.

Avoid putting mutable objects in a BST. Otherwise, when a mutable object that's in a BST is to be updated, always first remove it from the tree, then update it, then add it back.

'''


#%%
class BSTNode:

    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


#%%
# check if a given value is present in a BST

def search_bst(tree, key):
    return (tree if not tree or tree.data == key else search_bst(tree.left, key) if key < tree.data else search_bst(tree.right, key))

# Time complexity O(h), h is the height of the tree

#%% [markdown]
'''
### Tips
- With a BST you can iterate through elements in sorted order in time O(n)
- Some problems need a combination of a BST and a hashtable.
- The BST property is a global property. 
A binary tree may have the property that each node's key is greater than the key at its left child and smaller than the key at its right child, but it may not be a BST.

### Know binary search tree libraries
Python does not come with a built-in BST library. Other modules:
- sortedcontainers, pip install sortedcontainers
- bintrees, pip install bintrees, insert(e), discard(e), min_item()/max_item(), min_key()/max_key(), pop_min()/pop_max()

'''


#%%
# Test if a binary tree satisfies the BST property

def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_binary_tree_bst(tree.left, low_range, tree.data) and 
            is_binary_tree_bst(tree.right, tree.data, high_range))

# Time complexity O(n), space complexity O(h), h is the height of the tree.

#%%
## Alternatively, we can use the fact that an inorder traversal visits keys in sorted order.
## If an inorder traversal of a binary tree visits keys in sorted order, then that binary tree must be a BST.

# search for violations of the BST property in a BFS manner

import collections

def is_binary_tree_bst(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque(
        [QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

# Time complexity O(n), space complexity O(n)


#%%
