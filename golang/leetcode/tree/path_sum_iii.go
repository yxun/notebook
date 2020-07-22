package tree

// 437. Path Sum III

func pathSum(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}
	ret := pathSumStartWithRoot(root, sum) + pathSum(root.Left, sum) + pathSum(root.Right, sum)
	return ret
}

func pathSumStartWithRoot(root *TreeNode, sum int) int {
	if root == nil {
		return 0
	}
	ret := 0
	if root.Val == sum {
		ret++
	}
	ret += pathSumStartWithRoot(root.Left, sum-root.Val) + pathSumStartWithRoot(root.Right, sum-root.Val)
	return ret
}
