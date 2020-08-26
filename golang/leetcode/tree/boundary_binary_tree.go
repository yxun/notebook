package tree

// 545. Boundary of Binary Tree

func boundaryOfBinaryTree(root *TreeNode) []int {
	res := make([]int, 0)
	if root == nil {
		return res
	}
	res = append(res, root.Val)
	leftBoundary(root.Left, &res)
	leaves(root.Left, &res)
	leaves(root.Right, &res)
	rightBoundary(root.Right, &res)
	return res
}

func leftBoundary(node *TreeNode, res *[]int) {
	if node == nil || (node.Left == nil && node.Right == nil) {
		return
	}
	*res = append(*res, node.Val)
	if node.Left == nil {
		leftBoundary(node.Right, res)
	} else {
		leftBoundary(node.Left, res)
	}
}

func leaves(node *TreeNode, res *[]int) {
	if node == nil {
		return
	}
	if node.Left == nil && node.Right == nil {
		*res = append(*res, node.Val)
		return
	}
	leaves(node.Left, res)
	leaves(node.Right, res)
}

func rightBoundary(node *TreeNode, res *[]int) {
	if node == nil || (node.Right == nil && node.Left == nil) {
		return
	}
	if node.Right == nil {
		rightBoundary(node.Left, res)
	} else {
		rightBoundary(node.Right, res)
	}
	*res = append(*res, node.Val) // add after child visit
}
