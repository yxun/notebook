package tree

// 111. Minimum Depth of Binary Tree

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left, right := minDepth(root.Left), minDepth(root.Right)
	if left == 0 || right == 0 {
		return left + right + 1
	}
	return Min(left, right) + 1
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
