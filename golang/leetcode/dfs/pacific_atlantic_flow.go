package dfs

// 417. Pacific Atlantic Water Flow
var (
	directions [][]int
	m          int
	n          int
)

func pacificAtlantic(matrix [][]int) [][]int {
	directions = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	result := make([][]int, 0)
	if len(matrix) == 0 {
		return result
	}
	m, n = len(matrix), len(matrix[0])

	canReachP, canReachA := make([][]bool, m), make([][]bool, m)
	for i := range canReachP {
		canReachP[i] = make([]bool, n)
	}
	for i := range canReachA {
		canReachA[i] = make([]bool, n)
	}

	for i := 0; i < m; i++ {
		flowTrack(i, 0, canReachP, matrix)
		flowTrack(i, n-1, canReachA, matrix)
	}
	for i := 0; i < n; i++ {
		flowTrack(0, i, canReachP, matrix)
		flowTrack(m-1, i, canReachA, matrix)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if canReachP[i][j] && canReachA[i][j] {
				result = append(result, []int{i, j})
			}
		}
	}
	return result
}

func flowTrack(r int, c int, canReach [][]bool, matrix [][]int) {
	if canReach[r][c] {
		return
	}
	canReach[r][c] = true
	for _, d := range directions {
		nextR := r + d[0]
		nextC := c + d[1]
		if nextR < 0 || nextR >= m || nextC < 0 || nextC >= n || matrix[r][c] > matrix[nextR][nextC] {
			continue
		}
		flowTrack(nextR, nextC, canReach, matrix)
	}
}
