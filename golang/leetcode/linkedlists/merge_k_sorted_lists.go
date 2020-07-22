package linkedlists

// 23. Merge k Sorted Lists
import "container/heap"

type Node struct {
	Val   int
	Index int
	Node  *ListNode
}

type NodeQueue []*Node

func (q NodeQueue) Len() int {
	return len(q)
}

func (q NodeQueue) Less(i, j int) bool {
	return q[i].Val < q[j].Val
}

func (q NodeQueue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func (q *NodeQueue) Push(x interface{}) {
	*q = append(*q, x.(*Node))
}

func (q *NodeQueue) Pop() interface{} {
	old := *q
	x := old[len(old)-1]
	*q = old[:len(old)-1]
	return x
}

func mergeKLists(lists []*ListNode) *ListNode {
	h := &NodeQueue{}
	heap.Init(h)
	for i, head := range lists {
		if head != nil {
			heap.Push(h, &Node{Val: head.Val, Index: i, Node: head})
		}
	}

	cur := &ListNode{}
	dummy := cur
	for len(*h) != 0 {
		node := heap.Pop(h).(*Node)
		i, smallestNode := node.Index, node.Node
		cur.Next = smallestNode
		cur = cur.Next
		if smallestNode.Next != nil {
			heap.Push(h, &Node{Val: smallestNode.Next.Val, Index: i, Node: smallestNode.Next})
		}
	}
	return dummy.Next
}
