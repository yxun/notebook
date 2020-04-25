#%%
"""
- Flip Equivalent Binary Trees
- https://leetcode.com/problems/flip-equivalent-binary-trees/
- Medium

For a binary tree T, we can define a flip operation as follows: choose any node, and swap the left and right child subtrees.

A binary tree X is flip equivalent to a binary tree Y if and only if we can make X equal to Y after some number of flip operations.

Write a function that determines whether two binary trees are flip equivalent.  The trees are given by root nodes root1 and root2.

 

Example 1:

Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
Output: true
Explanation: We flipped at nodes with values 1, 3, and 5.
Flipped Trees Diagram
 

Note:

Each tree will have at most 100 nodes.
Each value in each tree will be a unique integer in the range [0, 99].
"""

#%%
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#%%
##
# root1 == root2
# node1.left == node2.left and node1.right == node2.right ; or node1.left == node2.right and node1.right == node2.left
# end: node == None, return true

class S1:

    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == root2 == None: 
            return True
        
        elif root1 and root2:
            if root1.val != root2.val: 
                return False
            else:
                return (self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)) or (self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left))
        else:
            return False
        
