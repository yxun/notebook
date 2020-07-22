package linkedlists

// 160. Intersection of Two Linked Lists

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	// A = a + c, B = b + c
	// a+c+b = b+c+a
	// when reach the tail of A, next to the head of B
	// when reach the tail of B, next to the head of A
	// if there is no intersaction, a+b=b+a, when l1 == l2 == nil, exit
	l1, l2 := headA, headB
	for l1 != l2 {
		if l1 == nil {
			l1 = headB
		} else {
			l1 = l1.Next
		}
		if l2 == nil {
			l2 = headA
		} else {
			l2 = l2.Next
		}
	}
	return l1
}
