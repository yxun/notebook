package tree

// 513. Find Bottom Left Tree Value

func findBottomLeftValue(root *TreeNode) int {
	// BFS, add right then add left
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	var node *TreeNode
	for len(queue) != 0 {
		node = queue[0]
		queue = queue[1:]
		if node.Right != nil {
			queue = append(queue, node.Right)
		}
		if node.Left != nil {
			queue = append(queue, node.Left)
		}
	}
	return node.Val
}
