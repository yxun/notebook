package tree

// 530. Minimum Absolute Difference in BST
import (
	"math"
)

var (
	pre *TreeNode
)

func getMinimumDifference(root *TreeNode) int {
	minDiff := math.MaxInt32
	pre = nil

	inOrderDiff(root, &minDiff)
	return minDiff
}

func inOrderDiff(node *TreeNode, minDiff *int) {
	if node == nil {
		return
	}
	inOrderDiff(node.Left, minDiff)
	if pre != nil {
		*minDiff = Min(*minDiff, node.Val-pre.Val)
	}
	pre = node
	inOrderDiff(node.Right, minDiff)
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
