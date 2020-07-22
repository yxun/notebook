package tree

// 236. Lowest Common Ancestor of a Binary Tree

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root == nil || root == p || root == q {
		return root
	}
	left, right := lowestCommonAncestor(root.Left, p, q), lowestCommonAncestor(root.Right, p, q)
	switch {
	case left == nil:
		{
			return right
		}
	case right == nil:
		{
			return left
		}
	case left != nil && right != nil:
		{
			return root
		}
	default:
		return root
	}
}
