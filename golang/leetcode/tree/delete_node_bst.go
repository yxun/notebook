package tree

// 450. Delete Node in a BST

func deleteNode(root *TreeNode, key int) *TreeNode {
	// if root.Val == key, three cases
	if root == nil {
		return root
	}
	if key > root.Val {
		root.Right = deleteNode(root.Right, key)
	} else if key < root.Val {
		root.Left = deleteNode(root.Left, key)
	} else if key == root.Val {
		if root.Left == nil {
			return root.Right
		} else if root.Right == nil {
			return root.Left
		} else {
			// find right subtree left most node
			cur := root.Right
			for cur.Left != nil {
				cur = cur.Left
			}
			cur.Left = root.Left
			return root.Right
		}
	}
	return root
}
