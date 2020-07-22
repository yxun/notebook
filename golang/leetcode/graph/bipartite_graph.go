package graph

// 785. Is Graph Bipartite?

func isBipartite(graph [][]int) bool {
	groups := make([]int, len(graph))
	for i := range groups {
		groups[i] = -1
	}
	for i := 0; i < len(graph); i++ {
		if groups[i] == -1 && !partition(i, 0, groups, graph) {
			return false
		}
	}
	return true
}

func partition(curNode int, curGroup int, groups []int, graph [][]int) bool {
	if groups[curNode] != -1 {
		return groups[curNode] == curGroup
	}
	groups[curNode] = curGroup
	for _, nextNode := range graph[curNode] {
		if !partition(nextNode, 1-curGroup, groups, graph) {
			return false
		}
	}
	return true
}
