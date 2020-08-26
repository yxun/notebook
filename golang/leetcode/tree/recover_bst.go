package tree

// 99. Recover Binary Search Tree

func recoverTree(root *TreeNode) {
	var pre, first, second *TreeNode
	_, first, second = inOrderRecover(root, pre, first, second)
	if first != nil && second != nil {
		first.Val, second.Val = second.Val, first.Val
	}
}

func inOrderRecover(root, pre, first, second *TreeNode) (*TreeNode, *TreeNode, *TreeNode) {
	if root == nil {
		return pre, first, second
	}
	pre, first, second = inOrderRecover(root.Left, pre, first, second)
	if pre != nil && pre.Val > root.Val {
		if first == nil {
			first = pre
		}
		second = root
	}
	// update prev
	pre = root
	pre, first, second = inOrderRecover(root.Right, pre, first, second)
	return pre, first, second
}
