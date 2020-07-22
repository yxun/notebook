package tree

// 110. Balanced Binary Tree
import "math"

func isBalanced(root *TreeNode) bool {
	result := true
	maxDepth(root, &result)
	return result
}

func maxDepth(root *TreeNode, result *bool) int {
	if root == nil {
		return 0
	}
	l, r := maxDepth(root.Left, result), maxDepth(root.Right, result)
	if math.Abs(float64(l-r)) > 1 {
		*result = false
	}
	return 1 + Max(l, r)
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
