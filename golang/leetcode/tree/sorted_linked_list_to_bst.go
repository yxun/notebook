package tree

// 109. Convert Sorted List to Binary Search Tree
type ListNode struct {
	Val  int
	Next *ListNode
}

func sortedListToBST(head *ListNode) *TreeNode {
	if head == nil {
		return nil
	}
	if head.Next == nil {
		return &TreeNode{Val: head.Val}
	}
	preMid := findPreMid(head)
	mid := preMid.Next
	preMid.Next = nil // break first half
	t := &TreeNode{Val: mid.Val}
	t.Left = sortedListToBST(head)
	t.Right = sortedListToBST(mid.Next)
	return t
}

func findPreMid(head *ListNode) *ListNode {
	slow, fast := head, head.Next
	pre := head
	for fast != nil && fast.Next != nil {
		pre = slow
		slow = slow.Next
		fast = fast.Next.Next
	}
	return pre
}
