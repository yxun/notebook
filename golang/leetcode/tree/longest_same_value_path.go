package tree

// 687. Longest Univalue Path

func longestUnivaluePath(root *TreeNode) int {
	ret := 0
	valuePath(root, &ret)
	return ret
}

func valuePath(root *TreeNode, ret *int) int {
	if root == nil {
		return 0
	}
	left := valuePath(root.Left, ret)
	right := valuePath(root.Right, ret)
	leftPath, rightPath := 0, 0
	if root.Left != nil && root.Left.Val == root.Val {
		leftPath = left + 1
	}
	if root.Right != nil && root.Right.Val == root.Val {
		rightPath = right + 1
	}
	*ret = Max(*ret, leftPath+rightPath)
	return Max(leftPath, rightPath)
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
