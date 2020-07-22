package tree

// 572. Subtree of Another Tree

// m, n  len(s), len(t)
// time O(m*n) worst case
// space worst case O(m), average case O(logm)

func isSubtree(s, t *TreeNode) bool {
	if s == nil {
		return false
	}
	return isSubtreeWithRoot(s, t) || isSubtree(s.Left, t) || isSubtree(s.Right, t)
}

func isSubtreeWithRoot(s, t *TreeNode) bool {
	if t == nil && s == nil {
		return true
	}
	if t == nil || s == nil {
		return false
	}
	if t.Val != s.Val {
		return false
	}
	return isSubtreeWithRoot(s.Left, t.Left) && isSubtreeWithRoot(s.Right, t.Right)
}
