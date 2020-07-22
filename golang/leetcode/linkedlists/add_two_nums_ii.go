package linkedlists

// 445. Add Two Numbers II
type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l1Stack, l2Stack := buildStack(l1), buildStack(l2)
	head := ListNode{-1, nil}
	carry := 0
	for len(l1Stack) != 0 || len(l2Stack) != 0 || carry != 0 {
		x, y := 0, 0
		if len(l1Stack) != 0 {
			x = l1Stack[len(l1Stack)-1]
			l1Stack = l1Stack[:len(l1Stack)-1]
		}
		if len(l2Stack) != 0 {
			y = l2Stack[len(l2Stack)-1]
			l2Stack = l2Stack[:len(l2Stack)-1]
		}
		sum := x + y + carry
		carry = sum / 10
		node := &ListNode{sum % 10, nil}
		node.Next = head.Next
		head.Next = node
	}
	return head.Next
}

func buildStack(l *ListNode) []int {
	stack := make([]int, 0)
	for l != nil {
		stack = append(stack, l.Val)
		l = l.Next
	}
	return stack
}
