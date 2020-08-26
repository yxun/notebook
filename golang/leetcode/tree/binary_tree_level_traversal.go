package tree

// 102. Binary Tree Level Order Traversal

func levelOrder(root *TreeNode) [][]int {
	// bfs
	queue := make([]*TreeNode, 0)
	res := make([][]int, 0)
	if root == nil {
		return res
	}
	queue = append(queue, root)
	for len(queue) != 0 {
		level := make([]int, 0)
		size := len(queue)
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			level = append(level, node.Val)
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		res = append(res, level)
	}
	return res
}
