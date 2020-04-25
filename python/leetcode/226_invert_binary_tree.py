#%%
"""
- Invert Binary Tree
- https://leetcode.com/problems/invert-binary-tree/
- Easy

Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

"""

#%%
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#%%
##
class S1:

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None: return root
        if root.left is None and root.right is None: return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
