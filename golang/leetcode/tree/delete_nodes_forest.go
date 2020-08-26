package tree

// 1110. Delete Nodes And Return Forest

// solve tree problem with recursion first
// if a node is root (has no parent) and isn't deleted, add it to the res

// time O(N), space O(H+N) H is the height of tree
func delNodes(root *TreeNode, to_delete []int) []*TreeNode {
	set := make(map[int]bool)
	for _, node := range to_delete {
		set[node] = true
	}

	res := make([]*TreeNode, 0)
	if !set[root.Val] {
		res = append(res, root)
	}
	dfsDelNodes(root, set, &res)
	return res
}

func dfsDelNodes(node *TreeNode, set map[int]bool, res *[]*TreeNode) *TreeNode {
	if node == nil {
		return nil
	}
	node.Left = dfsDelNodes(node.Left, set, res)
	node.Right = dfsDelNodes(node.Right, set, res)
	if set[node.Val] {
		if node.Left != nil {
			*res = append(*res, node.Left)
		}
		if node.Right != nil {
			*res = append(*res, node.Right)
		}
		return nil
	}
	return node
}
