package tree

// 235. Lowest Common Ancestor of a Binary Search Tree

func lowestCommonAncestorBST(root, p, q *TreeNode) *TreeNode {
	if root.Val > p.Val && root.Val > q.Val {
		return lowestCommonAncestorBST(root.Left, p, q)
	}
	if root.Val < p.Val && root.Val < q.Val {
		return lowestCommonAncestorBST(root.Right, p, q)
	}
	return root
}
