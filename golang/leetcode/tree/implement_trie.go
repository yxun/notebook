package tree

// 208. Implement Trie (Prefix Tree)

type Node struct {
	childs [26]*Node
	isLeaf bool
}

type Trie struct {
	root *Node
}

func Constructor() Trie {
	return Trie{
		root: &Node{},
	}
}

func (this *Trie) Insert(word string) {
	insert(word, this.root)
}

func insert(word string, node *Node) {
	if node == nil {
		return
	}
	if len(word) == 0 {
		node.isLeaf = true
		return
	}
	index := word[0] - 'a'
	if node.childs[index] == nil {
		node.childs[index] = &Node{}
	}
	insert(word[1:], node.childs[index])
}

func (this *Trie) Search(word string) bool {
	return search(word, this.root)
}

func search(word string, node *Node) bool {
	if node == nil {
		return false
	}
	if len(word) == 0 {
		return node.isLeaf
	}
	index := word[0] - 'a'
	return search(word[1:], node.childs[index])
}

func (this *Trie) StartsWith(prefix string) bool {
	return startWith(prefix, this.root)
}

func startWith(prefix string, node *Node) bool {
	if node == nil {
		return false
	}
	if len(prefix) == 0 {
		return true
	}
	index := prefix[0] - 'a'
	return startWith(prefix[1:], node.childs[index])
}
