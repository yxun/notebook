package arrays

// 526. Beautiful Arrangement

// backtracking, try every possible number at each position
func countArrangement(N int) int {
	if N == 0 {
		return 0
	}
	res := 0
	visited := make([]int, N+1)
	dfsArrange(N, 1, visited, &res)
	return res
}

func dfsArrange(N, start int, visited []int, res *int) {
	if start > N {
		*res++
		return
	}
	for i := 1; i <= N; i++ {
		if visited[i] == 0 && (i%start == 0 || start%i == 0) {
			visited[i] = 1
			dfsArrange(N, start+1, visited, res)
			// backtrack
			visited[i] = 0
		}
	}
}
