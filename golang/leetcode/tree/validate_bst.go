package tree

// 98. Validate Binary Search Tree
import "math"

func isValidBST(root *TreeNode) bool {
	return isBST(root).valid
}

type ResultType struct {
	max   int
	min   int
	valid bool
}

func isBST(root *TreeNode) (ret ResultType) {
	if root == nil {
		ret.max = math.MinInt64
		ret.min = math.MaxInt64
		ret.valid = true
		return
	}

	left, right := isBST(root.Left), isBST(root.Right)
	if root.Val > left.max && root.Val < right.min && left.valid && right.valid {
		ret.valid = true
	}

	ret.max = Max(Max(left.max, right.max), root.Val)
	ret.min = Min(Min(left.min, right.min), root.Val)
	return
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
