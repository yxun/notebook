package tree

// 979. Distribute Coins in Binary Tree

import "math"

// dfs or recursive, count number of moves from child to parent
func distributeCoins(root *TreeNode) int {
	res := 0
	if root.Left != nil {
		res += distributeCoins(root.Left)
		root.Val += root.Left.Val - 1
		res += int(math.Abs(float64(root.Left.Val - 1)))
	}
	if root.Right != nil {
		res += distributeCoins(root.Right)
		root.Val += root.Right.Val - 1
		res += int(math.Abs(float64(root.Right.Val - 1)))
	}
	return res
}
