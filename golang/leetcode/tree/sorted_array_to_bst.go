package tree

// 108. Convert Sorted Array to Binary Search Tree

func sortedArrayToBST(nums []int) *TreeNode {
	return toBST(nums, 0, len(nums)-1)
}

func toBST(nums []int, l, h int) *TreeNode {
	if l > h {
		return nil
	}
	mid := l + (h-l)/2
	root := &TreeNode{Val: nums[mid]}
	root.Left = toBST(nums, l, mid-1)
	root.Right = toBST(nums, mid+1, h)
	return root
}
