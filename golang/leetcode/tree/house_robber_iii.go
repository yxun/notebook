package tree

// 337. House Robber III

func rob(root *TreeNode) int {
	if root == nil {
		return 0
	}
	val1 := root.Val
	if root.Left != nil {
		val1 += rob(root.Left.Left) + rob(root.Left.Right)
	}
	if root.Right != nil {
		val1 += rob(root.Right.Left) + rob(root.Right.Right)
	}
	val2 := rob(root.Left) + rob(root.Right)
	return Max(val1, val2)
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
