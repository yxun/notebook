package linkedlists

// 19. Remove Nth Node From End of List

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	if head == nil {
		return head
	}
	slow, fast := head, head
	for i := 0; i < n; i++ {
		fast = fast.Next
	}
	if fast == nil {
		return head.Next
	}

	for fast.Next != nil {
		slow = slow.Next
		fast = fast.Next
	}
	slow.Next = slow.Next.Next
	return head
}
