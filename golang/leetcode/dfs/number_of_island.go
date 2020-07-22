package dfs

// 200. Number of Islands

func numIslands(grid [][]byte) int {
	if len(grid) == 0 {
		return 0
	}
	directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	result := 0
	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			if grid[i][j] != '0' {
				numTrack(grid, i, j, directions)
				result++
			}
		}
	}
	return result
}

func numTrack(grid [][]byte, i int, j int, directions [][]int) {
	if i < 0 || i >= len(grid) || j < 0 || j >= len(grid[0]) || grid[i][j] == '0' {
		return
	}
	grid[i][j] = '0'
	for _, d := range directions {
		numTrack(grid, i+d[0], j+d[1], directions)
	}
}
