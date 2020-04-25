#%%
"""
- Flip Binary Tree (Binary Tree Upside Down)
- https://leetcode.com/problems/binary-tree-upside-down/
- Medium
"""

#%%
"""
Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes. Return the new root.

Example:

Input: [1,2,3,4,5]

    1
   / \
  2   3
 / \
4   5

Output: return the root of the binary tree [4,5,2,#,#,3,1]

   4
  / \
 5   2
    / \
   3   1  
Clarification:

Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is serialized on OJ.

The serialization of a binary tree follows a level order traversal, where '#' signifies a path terminator where no node exists below.

Here's an example:

   1
  / \
 2   3
    /
   4
    \
     5
The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
"""

#%%
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#%%
class S:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """

        if root is None: return root
        if root.left is None and root.right is None: return root

        newRoot = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None

        return newRoot

#%%
from queue import Queue
class Node:

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def flipBinaryTree(root):
    # Base case
    if root is None:
        return root
    
    if root.left is None and root.right is None:
        return root

    # Recursively call the same method
    flippedRoot = flipBinaryTree(root.left)

    # Rearranging main root Node after returning
    # from recursive call
    root.left.left = root.right
    root.left.right = root
    root.left = root.right = None

    return flippedRoot

# Iterative method to do the level order traversal
# line by line
def printLevelOrder(root):
    # Base case
    if root is None:
        return
    
    # Create an empty queue for level order traversal
    
    q = Queue()

    # Enqueue root and initialize height
    q.put(root)

    while True:
        # nodeCount (queue size) indicates number
        # of nodes at current level
        nodeCount = q.qsize()
        if nodeCount == 0:
            break

        # Dequeue all nodes of current level and
        # Enqueue all nodes of next level
        while nodeCount > 0:
            node = q.get()
            print(node.data, end=' ')
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)
            nodeCount -= 1
        print()

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)

print("Level order traversal of given tree")
printLevelOrder(root)

root = flipBinaryTree(root)

print("\nLevel Order traversal of the flipped tree")
printLevelOrder(root)

#%%
