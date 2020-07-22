package tree

// 404. Sum of Left Leaves

func sumOfLeftLeaves(root *TreeNode) int {
	if root == nil {
		return 0
	}
	if isLeaf(root.Left) {
		return root.Left.Val + sumOfLeftLeaves(root.Right)
	}
	return sumOfLeftLeaves(root.Left) + sumOfLeftLeaves(root.Right)
}

func isLeaf(node *TreeNode) bool {
	if node == nil {
		return false
	}
	return node.Left == nil && node.Right == nil
}
