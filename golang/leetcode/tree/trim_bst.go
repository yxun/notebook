package tree

// 669. Trim a Binary Search Tree

func trimBST(root *TreeNode, L, R int) *TreeNode {
	if root == nil {
		return nil
	}
	if root.Val > R {
		return trimBST(root.Left, L, R)
	}
	if root.Val < L {
		return trimBST(root.Right, L, R)
	}
	root.Left = trimBST(root.Left, L, R)
	root.Right = trimBST(root.Right, L, R)
	return root
}
