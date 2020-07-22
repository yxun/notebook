package tree

// 671. Second Minimum Node In a Binary Tree

func findSecondMinimumValue(root *TreeNode) int {
	if root == nil {
		return -1
	}
	if root.Left == nil && root.Right == nil {
		return -1
	}
	leftVal, rightVal := root.Left.Val, root.Right.Val
	if leftVal == root.Val {
		leftVal = findSecondMinimumValue(root.Left)
	}
	if rightVal == root.Val {
		rightVal = findSecondMinimumValue(root.Right)
	}
	if leftVal != -1 && rightVal != -1 {
		return Min(leftVal, rightVal)
	} else if leftVal != -1 {
		return leftVal
	} else {
		return rightVal
	}
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
