package tree

// 230. Kth Smallest Element in a BST

func kthSmallest(root *TreeNode, k int) int {
	cnt := 0
	var val int
	inOrder(root, k, &cnt, &val)
	return val
}

func inOrder(node *TreeNode, k int, cnt, val *int) {
	if node == nil {
		return
	}
	inOrder(node.Left, k, cnt, val)
	*cnt++
	if *cnt == k {
		*val = node.Val
		return
	}
	inOrder(node.Right, k, cnt, val)
}
