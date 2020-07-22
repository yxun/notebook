package tree

// 95. Unique Binary Search Trees II

func generateTrees(n int) []*TreeNode {
	if n == 0 {
		return nil
	}
	return generate(1, n)
}

func generate(start, end int) []*TreeNode {
	if start > end {
		return []*TreeNode{nil}
	}
	ans := make([]*TreeNode, 0)
	for i := start; i <= end; i++ {
		// divide generate left tree and right tree
		// i is root
		lefts := generate(start, i-1)
		rights := generate(i+1, end)
		// connect left and right trees
		for j := 0; j < len(lefts); j++ {
			for k := 0; k < len(rights); k++ {
				root := &TreeNode{Val: i}
				root.Left = lefts[j]
				root.Right = rights[k]
				ans = append(ans, root)
			}
		}
	}
	return ans
}
