package linkedlists

// 328. Odd Even Linked List

func oddEvenList(head *ListNode) *ListNode {
	if head == nil {
		return head
	}
	odd, even := head, head.Next
	evenHead := even
	for even != nil && even.Next != nil {
		odd.Next = odd.Next.Next
		odd = odd.Next
		even.Next = even.Next.Next
		even = even.Next
	}
	odd.Next = evenHead
	return head
}
