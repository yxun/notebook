package tree

// 543. Diameter of Binary Tree

func diameterOfBinaryTree(root *TreeNode) int {
	max := 0
	depth(root, &max)
	return max
}

func depth(node *TreeNode, max *int) int {
	if node == nil {
		return 0
	}
	leftDepth, rightDepth := depth(node.Left, max), depth(node.Right, max)
	*max = Max(*max, leftDepth+rightDepth)
	return Max(leftDepth, rightDepth) + 1
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
