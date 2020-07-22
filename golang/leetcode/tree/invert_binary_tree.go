package tree

// 226. Invert Binary Tree

func invertTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	left := root.Left
	root.Left = invertTree(root.Right)
	root.Right = invertTree(left)
	return root
}
