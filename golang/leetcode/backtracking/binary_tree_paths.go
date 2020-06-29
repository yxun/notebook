package backtracking

import (
	"strconv"
	"strings"
)

// 257. Binary Tree Paths

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func binaryTreePaths(root *TreeNode) []string {
	paths := make([]string, 0)
	if root == nil {
		return paths
	}
	values := make([]int, 0)
	pathTrack(root, values, &paths)
	return paths
}

func pathTrack(node *TreeNode, values []int, paths *[]string) {
	if node == nil {
		return
	}
	values = append(values, node.Val)
	if isLeaf(node) {
		*paths = append(*paths, buildPath(values))
	} else {
		pathTrack(node.Left, values, paths)
		pathTrack(node.Right, values, paths)
	}

	values = values[:len(values)-1]
}

func isLeaf(node *TreeNode) bool {
	return node.Left == nil && node.Right == nil
}

func buildPath(values []int) string {
	var str strings.Builder
	for i := 0; i < len(values); i++ {
		str.WriteString(strconv.Itoa(values[i]))
		if i != len(values)-1 {
			str.WriteString("->")
		}
	}
	return str.String()
}
