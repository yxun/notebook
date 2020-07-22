package tree

// 104. Maximum Depth of Binary Tree

func maxDepth2(root *TreeNode) int {
	if root == nil {
		return 0
	}
	left, right := maxDepth2(root.Left), maxDepth2(root.Right)
	return Max(left, right) + 1
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
