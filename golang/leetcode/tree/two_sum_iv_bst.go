package tree

// 653. Two Sum IV - Input is a BST

func findTarget(root *TreeNode, k int) bool {
	nums := make([]int, 0)
	treeToArray(root, &nums)
	l, h := 0, len(nums)-1
	for l < h {
		sum := nums[l] + nums[h]
		if sum == k {
			return true
		} else if sum > k {
			h--
		} else {
			l++
		}
	}
	return false
}

func treeToArray(root *TreeNode, nums *[]int) {
	if root == nil {
		return
	}
	treeToArray(root.Left, nums)
	*nums = append(*nums, root.Val)
	treeToArray(root.Right, nums)
}
