package tree

// 677. Map Sum Pairs

type MapSum struct {
	Val   int
	Child []*MapSum
}

func Constructor2() MapSum {
	child := make([]*MapSum, 26)
	return MapSum{
		Val:   0,
		Child: child,
	}
}

func (this *MapSum) Insert(key string, val int) {
	if this == nil {
		return
	}
	if len(key) == 0 {
		this.Val = val
		return
	}
	index := key[0] - 'a'
	if this.Child[index] == nil {
		newNode := Constructor2()
		this.Child[index] = &newNode
	}
	this.Child[index].Insert(key[1:], val)
}

func (this *MapSum) Sum(prefix string) int {
	if this == nil {
		return 0
	}
	if len(prefix) != 0 {
		index := prefix[0] - 'a'
		return this.Child[index].Sum(prefix[1:])
	}
	sum := this.Val
	for _, child := range this.Child {
		sum += child.Sum(prefix)
	}
	return sum
}
