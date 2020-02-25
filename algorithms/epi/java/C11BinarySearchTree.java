
import java.util.Queue;
import java.util.LinkedList; 


public class C11BinarySearchTree {
    public static class BSTNode<T> {
        public T data;
        public BSTNode<T> left, right;
    }

    // Binary search trees boot camp
    public static BSTNode<Integer> searchBST(BSTNode<Integer> tree, int key) {
        return tree == null || tree.data == key 
            ? tree
            : key < tree.data ? searchBST(tree.left, key)
                            : searchBST(tree.right, key);
    }
    // time O(h)

    // Know your binary search tree libraries
    // TreeSet and TreeMap
    // The iterator returned by iterator() traverses keys in ascending order
    // first()/last() yield the smallest and largest keys in the tree
    // lower(12)/higher(3), floor(4.9)/ceiling(5.7), headSet(10),tailSet(5),subSet(1,12)

    // Test if a binary tree satisfies the BST property
    // The first approach is to check constraints on the values for each subtree.
    // if all nodes in a tree must have keys in the range [l,u], and the key at the root is w (w must be between [l,u]),
    // then all keys in the left subtree must be in the range [l,w], and all keys stored in the right subtree must be in the range [w,u]
    public static boolean isBinaryTreeBST(BinaryTreeNode<Integer> tree) {
        return areKeysInRange(tree, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private static boolean areKeysInRange(BinaryTreeNode<Integer> tree, Integer lower, Integer upper) {
        if (tree == null) {
            return true;
        } else if (Integer.compare(tree.data, lower) < 0 || Integer.compare(tree.data, upper) > 0) {
            return false;
        }

        return areKeysInRange(tree.left, lower, tree.data) && areKeysInRange(tree.right, tree.data, upper);
    }
    // time O(n), space O(h)

    // Alternatively, an inorder traversal visits keys in sorted order. 
    // If an inorder traversal of a binary tree visits keys in sorted order, then that binary tree must be a BST
    // We can search for violations of the BST property in a BFS manner, thereby reducing the time when the property is violated at a node whose depth is small
    // We use a queue, where each queue entry contains a node, as well as an upper and a lower bound on the keys stored at the subtree rooted at that node.

    public static class QueueEntry {
        public BinaryTreeNode<Integer> treeNode;
        public Integer lowerBound, upperBound;

        public QueueEntry(BinaryTreeNode<Integer> treeNode, Integer lowerBound, Integer upperBound) {
            this.treeNode = treeNode;
            this.lowerBound = lowerBound;
            this.upperBound = upperBound;
        }
    }

    public static boolean isBinaryTreeBST2(BinaryTreeNode<Integer> tree) {
        Queue<QueueEntry> BFSQueue = new LinkedList<>();
        BFSQueue.add(new QueueEntry(tree, Integer.MIN_VALUE, Integer.MAX_VALUE));

        QueueEntry headEntry;
        while ((headEntry = BFSQueue.poll()) != null) {
            if (headEntry.treeNode != null) {
                if (headEntry.treeNode.data < headEntry.lowerBound || headEntry.treeNode.data > headEntry.upperBound) {
                    return false;
                }

                BFSQueue.add(new QueueEntry(headEntry.treeNode.left, 
                                            headEntry.lowerBound, 
                                            headEntry.treeNode.data));
                BFSQueue.add(new QueueEntry(headEntry.treeNode.right,
                                            headEntry.treeNode.data,
                                            headEntry.upperBound));
            }
        }
        return true;
    }
    // time O(n), space O(n)
}
