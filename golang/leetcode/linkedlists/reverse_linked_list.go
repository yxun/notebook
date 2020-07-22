package linkedlists

// 206. Reverse Linked List

// iterative
func reverseList1(head *ListNode) *ListNode {
	newHead := &ListNode{}
	for head != nil {
		next := head.Next
		head.Next = newHead.Next
		newHead.Next = head
		head = next
	}
	return newHead.Next
}

// recurion
func reverseList2(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	next := head.Next
	newHead := reverseList2(next)
	next.Next = head
	head.Next = nil
	return newHead
}
