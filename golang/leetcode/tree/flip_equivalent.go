package tree

// 951. Flip Equivalent Binary Trees

func flipEquiv(root1, root2 *TreeNode) bool {
	if root1 == nil {
		return root2 == nil
	}
	if root2 == nil {
		return root1 == nil
	}
	if root1.Val != root2.Val {
		return false
	}

	return (flipEquiv(root1.Left, root2.Left) && flipEquiv(root1.Right, root2.Right)) || (flipEquiv(root1.Left, root2.Right) && flipEquiv(root1.Right, root2.Left))
}
