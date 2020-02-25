
// prototype
class BinaryTreeNode<T> {
    public T data;
    public BinaryTreeNode<T> left, right;
}


public class C6BinaryTrees {

    // The depth of a node is the number of nodes on the search path from the root to n, not including n itself
    // The height of a binary tree is the maximum depth of any node in that tree
    // A level of a tree is all nodes at the same depth
    // A full binary tree is a binary tree in which every node other than the leaves has two children
    // A pefect binary tree is a full binary tree in which all leaves are at the same depth
    
    // the number of nonleaf nodes in a full binary tree is one less than the number of leaves
    // A perfect binary tree of height h contains 2^(h+1)-1 nodes, of which 2^h leaves
    // A complete binary tree on n nodes has height logn
    // A left-skewed tree is a tree in which no node has a right child
    // A right-skewed tree is a tree in which no node has a left child

    // inorder traversal: left subtree, root, right substree
    // preorder traversal: root, left subtree, right subtree
    // postorder traversal: left subtree, right subtree, root

    // O(h) complexity, where h is the tree height, translate into O(logn) complexity for balanced trees, but O(n) for skewed trees
    // It's easy to make the mistake of treating a node that has a single child as a leaf

    // Test if a binary tree is height-balanced
    // the difference in the height of its left and right subtrees is at most one

    private static class BalanceStatusWithHeight {
        public boolean balanced;
        public int height;
    
        public BalanceStatusWithHeight(boolean balanced, int height) {
            this.balanced = balanced;
            this.height = height;
        }
    }

    public static boolean isBalanced(BinaryTreeNode<Integer> tree) {
        return checkBalanced(tree).balanced;
    }

    private static BalanceStatusWithHeight checkBalanced(BinaryTreeNode<Integer> tree) {
        if (tree == null) {
            return new BalanceStatusWithHeight(true, -1);  // Base case
        }

        BalanceStatusWithHeight leftResult = checkBalanced(tree.left);
        if (!leftResult.balanced) {
            return leftResult;   // Left subtree is not balanced
        }

        BalanceStatusWithHeight rightResult = checkBalanced(tree.right);
        if (!rightResult.balanced) {
            return rightResult;  // Right subtree is not balanced
        }

        boolean isBalanced = Math.abs(leftResult.height - rightResult.height) <= 1;
        int height = Math.max(leftResult.height, rightResult.height) + 1;
        return new BalanceStatusWithHeight(isBalanced, height);
    }
    // postorder traveral, time O(n), space O(h)
}


