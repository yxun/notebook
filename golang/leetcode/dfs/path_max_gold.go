package dfs

// 1219. Path with Maximum Gold

// dfs + backtracking
func getMaximumGold(grid [][]int) int {
	directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	if len(grid) == 0 {
		return 0
	}

	m, n := len(grid), len(grid[0])
	result := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			result = Max(result, findMaxGold(grid, i, j, directions))
		}
	}
	return result
}

func findMaxGold(grid [][]int, r int, c int, directions [][]int) int {
	if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] == 0 {
		return 0
	}
	gold := grid[r][c]
	grid[r][c] = 0 // mark as visited
	maxGold := 0   // local max
	for _, d := range directions {
		maxGold = Max(maxGold, findMaxGold(grid, r+d[0], c+d[1], directions))
	}
	grid[r][c] = gold // backtracking
	return maxGold + gold
}

/*
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
*/
