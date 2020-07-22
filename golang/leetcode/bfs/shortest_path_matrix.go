package bfs

// 1091. Shortest Path in Binary Matrix

func shortestPathBinaryMatrix(grid [][]int) int {
	directions := [][]int{{1, -1}, {1, 0}, {1, 1}, {0, -1}, {0, 1}, {-1, -1}, {-1, 0}, {-1, 1}}
	m, n := len(grid), len(grid[0])
	if grid[0][0] == 1 || grid[m-1][n-1] == 1 {
		return -1
	}
	queue := make([][]int, 0)
	queue = append(queue, []int{0, 0})
	result := 0
	for len(queue) != 0 {
		size := len(queue)
		result++
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			cr, cc := cur[0], cur[1]
			grid[cr][cc] = 1 // mark
			if cr == m-1 && cc == n-1 {
				return result
			}

			for _, d := range directions {
				nr, nc := cr+d[0], cc+d[1]
				if nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 1 {
					continue
				}
				queue = append(queue, []int{nr, nc})
				grid[nr][nc] = 1
			}
		}
	}
	return -1
}
