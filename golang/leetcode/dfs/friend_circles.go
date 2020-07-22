package dfs

// 547. Friend Circles

func findCircleNum(M [][]int) int {
	n := len(M)
	result := 0
	visited := make([]bool, n)
	for i := 0; i < n; i++ {
		if !visited[i] {
			circleTrack(M, i, visited, n)
			result++
		}
	}
	return result
}

func circleTrack(M [][]int, i int, visited []bool, n int) {
	visited[i] = true
	for k := 0; k < n; k++ {
		if M[i][k] == 1 && !visited[k] {
			circleTrack(M, k, visited, n)
		}
	}
}
