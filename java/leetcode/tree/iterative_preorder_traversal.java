/**
 * 144. Binary Tree Preorder Traversal
 * Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
 */

/**
 * preorder
 * void dfs(TreeNode root) {
 *      visit(root);
 *      dfs(root.left);
 *      dfs(root.right);
 * }
 * 
 * inorder
 * void dfs(TreeNode root) {
 *      dfs(root.left);
 *      visit(root);
 *      dfs(root.right);
 * }
 * 
 * postorder
 * void dfs(TreeNode root) {
 *      dfs(root.left);
 *      dfs(root.right);
 *      visit(root);
 * }
 * 
 */

import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

import javax.swing.tree.TreeNode;

public class iterative_preorder_traversal {

    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> ret = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);
        while(!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node == null) continue;
            ret.add(node.val);
            stack.push(node.right);     // stack push right and visit left first
            stack.push(node.left);
        }
        return ret;
    }
}