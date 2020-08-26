package tree

// 173. Binary Search Tree Iterator

type BSTIterator struct {
	nodes *[]int
	cur   int
}

func IterConstructor(root *TreeNode) BSTIterator {
	// inorder
	iter := BSTIterator{
		nodes: new([]int),
		cur:   -1,
	}
	inOrderIter(root, iter.nodes)
	return iter
}

func inOrderIter(node *TreeNode, res *[]int) {
	if node == nil {
		return
	}
	inOrderIter(node.Left, res)
	*res = append(*res, node.Val)
	inOrderIter(node.Right, res)
}

/** @return the next smallest number */
func (this *BSTIterator) Next() int {
	if this.HasNext() {
		this.cur = this.cur + 1
	}
	return (*this.nodes)[this.cur]
}

/** @return whether we have a next smallest number */
func (this *BSTIterator) HasNext() bool {
	return this.cur+1 < len(*this.nodes)
}
