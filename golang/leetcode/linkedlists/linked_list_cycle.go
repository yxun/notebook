package linkedlists

// 141. Linked List Cycle

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	l1, l2 := head, head.Next
	for l1 != nil && l2 != nil && l2.Next != nil {
		if l1 == l2 {
			return true
		}
		l1, l2 = l1.Next, l2.Next.Next

	}
	return false
}
