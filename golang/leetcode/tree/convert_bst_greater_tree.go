package tree

// 538. Convert BST to Greater Tree

func convertBST(root *TreeNode) *TreeNode {
	sum := 0
	traver(root, &sum)
	return root
}

func traver(node *TreeNode, sum *int) {
	if node == nil {
		return
	}
	traver(node.Right, sum)
	*sum += node.Val
	node.Val = *sum
	traver(node.Left, sum)
}
