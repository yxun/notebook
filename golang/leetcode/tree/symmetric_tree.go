package tree

// 101. Symmetric Tree

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return checkSymmetric(root.Left, root.Right)
}

func checkSymmetric(t1, t2 *TreeNode) bool {
	if t1 == nil && t2 == nil {
		return true
	}
	if t1 == nil || t2 == nil {
		return false
	}
	if t1.Val != t2.Val {
		return false
	}
	return checkSymmetric(t1.Left, t2.Right) && checkSymmetric(t1.Right, t2.Left)
}
