package dfs

// 695. Max Area of

func maxAreaOfIsland(grid [][]int) int {
	directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}

	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	result := 0

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			result = Max(result, areaTrack(grid, i, j, directions))
		}
	}
	return result
}

func areaTrack(grid [][]int, r int, c int, directions [][]int) int {
	if r < 0 || r >= len(grid) || c < 0 || c >= len(grid[0]) || grid[r][c] == 0 {
		return 0
	}
	grid[r][c] = 0
	area := 1
	for _, d := range directions {
		area += areaTrack(grid, r+d[0], c+d[1], directions)
	}
	return area
}

func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
