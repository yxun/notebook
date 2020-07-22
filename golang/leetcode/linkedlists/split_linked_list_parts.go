package linkedlists

// 725. Split Linked List in Parts

func splitListToParts(root *ListNode, k int) []*ListNode {
	N := 0
	cur := root
	for cur != nil {
		N++
		cur = cur.Next
	}
	mod, size := N%k, N/k
	ret := make([]*ListNode, k)
	cur = root
	curSize := 0
	for i := 0; cur != nil && i < k; i++ {
		ret[i] = cur
		if mod > 0 {
			curSize = size + 1
			mod--
		} else {
			curSize = size
			mod--
		}
		for j := 0; j < curSize-1; j++ {
			cur = cur.Next
		}
		next := cur.Next
		cur.Next = nil
		cur = next
	}
	return ret
}
