package linkedlists

// 83. Remove Duplicates from Sorted List

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	head.Next = deleteDuplicates(head.Next)
	if head.Val == head.Next.Val {
		return head.Next
	}
	return head
}
