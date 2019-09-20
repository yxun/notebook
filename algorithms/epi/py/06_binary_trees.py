#%% [markdown]
'''
A binary tree is either empty, or a root node r together with a left binary tree and a right binary tree.
With the exception of the root, every node has a unique parent.

### Concepts
- subtree
- child
- parent
- search path: the sequence from the root to the node.
- ancestor: a node lies on the search path from the root to d. A node is an ancestor and descendant of itself.
- descendant
- leaf: a node that has no descendants except for itself
- depth: the number of nodes on the search path from the root to n, not including n itself.
- height: the maximum depth of any node in the tree.
- level: all nodes at the same depth.
- a full binary tree: a binary tree in which every node other than the leaves has two children.
- a complete binary tree: a binary tree in which every level, except possibly the last, is completely filled.
- a perfect binary tree: a full binary tree in which all leaves are at the same depth.
- a left-skewed tree: a tree in which no node has a right child.
- a right-skewed tree: a tree in which no node has a left child.

'''

'''
### Inductions
- The number of nonleaf nodes in a full binary tree is one less than the number of leaves.
- A perfect binary tree of height h contains exactly 2^(h+1) - 1 nodes, of which 2^h are leaves.
- A complete binary tree on n nodes has height floor(logn).
'''

#%%
class BinaryTreeNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


#%% [markdown]
'''
### tree traversing:
- inorder traversal: traverse the left subtree, visit the root, then traverse the right subtree.
- preorder traversal: visit the root, traverse the left subtree, then traverse the right subtree.
- postorder traversal: traverse the left subtree, traverse the right subtree, and then visit the root.

Let T be a binary tree of n nodes, with height h. Implemented recursively, these traversals have O(n) time complexity and O(h) additional space complexity. (dictated by the maximum depth of the function call stack.)
The minimum value for h is logn (complete binary tree) and the maximum value for h is n (skewed tree).
If each node has a parent field, the traversals can be done with O(1) additional space complexity.
'''

#%% [markdown]
'''
### Tips:
- Recursive algorithms are well-suited to problems on trees.
- Some tree problems have simple brute-force solutions that use O(n) space solution, but subtler solutions that uses the existing tree nodes to reduce space complexity to O(1).
- Consider left- and right- skewed trees when doing complexity analysis.
- If each node has a parent field, use it to make your code simpler.
- It's easy to make the mistake of treating a node that has a single child as a leaf.
'''


#%%
# Test if a binary tree is height-balanced
# A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left and right subtrees is at most one.

# we do not need to store the heights of all nodes at the same time. Once we are done with a subtree, all we need is whether it is height-balanced, and if so, what its height is.
# This program implements a postorder traversal. Time complexity O(n), Sapce complexity O(h) space bound.


import collections

def is_balanced_binary_tree(tree):
    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced', 'height')
    )

    # First value of the return value indicates if tree is balanced, and if
    # balanced the second value of the return value is the height of tree.
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1)   # Base case.

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            # Left subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced.
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced 


#%% [markdown]
'''
### Variant
- Write a program that returns the size of the largest subtree that is complete.
- Define a node in a binary tree to be k-balanced if the difference in the number of nodes in its left and right subtrees is no more than k.
    Design an algorithm that takes as input a binary tree and positive integer k, and returns a node in the binary tree such that the node is not k-balanced,
    but all of its descendants are k-balanced.

'''


#%%
