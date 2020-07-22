package dfs

// 684. Redundant Connection

func findRedundantConnection(edges [][]int) []int {
	// dfs
	sets := make([]int, len(edges)+1)
	for _, edge := range edges {
		u, v := find(sets, edge[0]), find(sets, edge[1])
		if u == v {
			return edge
		}
		sets[u] = v
	}
	return []int{}
}

func find(sets []int, v int) int {
	if sets[v] == 0 {
		return v
	}
	return find(sets, sets[v])
}
