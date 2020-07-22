package linkedlists

// 24. Swap Nodes in Pairs

func swapPairs(head *ListNode) *ListNode {
	node := &ListNode{}
	node.Next = head
	pre := node
	for pre.Next != nil && pre.Next.Next != nil {
		l1, l2 := pre.Next, pre.Next.Next
		next := l2.Next
		l1.Next, l2.Next, pre.Next = next, l1, l2

		pre = l1
	}
	return node.Next
}
