package tree

// 103. Binary Tree Zigzag Level Order Traversal

func zigzagLevelOrder(root *TreeNode) [][]int {
	res := make([][]int, 0)
	zigzagTravel(&res, 0, root)
	return res
}

func zigzagTravel(res *[][]int, level int, node *TreeNode) {
	if node == nil {
		return
	}
	if len(*res) <= level {
		*res = append(*res, make([]int, 0))
	}
	if level%2 == 0 {
		(*res)[level] = append((*res)[level], node.Val)
	} else {
		(*res)[level] = append([]int{node.Val}, (*res)[level]...)
	}
	zigzagTravel(res, level+1, node.Left)
	zigzagTravel(res, level+1, node.Right)
}
