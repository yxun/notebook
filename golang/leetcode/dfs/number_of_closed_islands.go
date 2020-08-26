package dfs

// 1254. Number of Closed Islands

func closedIsland(grid [][]int) int {
	directions = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	if len(grid) == 0 {
		return 0
	}
	m, n = len(grid), len(grid[0])

	for i := 0; i < m; i++ {
		islandTrack(grid, i, 0)
		islandTrack(grid, i, n-1)
	}
	for i := 0; i < n; i++ {
		islandTrack(grid, 0, i)
		islandTrack(grid, m-1, i)
	}

	res := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if grid[i][j] == 0 {
				islandTrack(grid, i, j)
				res++
			}
		}
	}
	return res
}

func islandTrack(grid [][]int, r int, c int) {
	if r < 0 || r >= m || c < 0 || c >= n || grid[r][c] != 0 {
		return
	}
	grid[r][c] = -1
	for _, d := range directions {
		islandTrack(grid, r+d[0], c+d[1])
	}
}
