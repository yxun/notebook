package tree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// 637. Average of Levels in Binary Tree

func averageOfLevels(root *TreeNode) []float64 {
	// BFS
	ret := make([]float64, 0)
	if root == nil {
		return ret
	}
	queue := make([]*TreeNode, 0)
	queue = append(queue, root)
	for len(queue) != 0 {
		size := len(queue)
		sum := 0
		for i := 0; i < size; i++ {
			node := queue[0]
			queue = queue[1:]
			sum += node.Val
			if node.Left != nil {
				queue = append(queue, node.Left)
			}
			if node.Right != nil {
				queue = append(queue, node.Right)
			}
		}
		ret = append(ret, float64(sum)/float64(size))
	}
	return ret
}
