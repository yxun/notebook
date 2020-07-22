package bfs

// 279. Perfect Squares

func numSquares(n int) int {
	squares := generateSquares(n)
	queue := make([]int, 0)
	visited := make([]bool, n+1)

	queue = append(queue, n)
	visited[n] = true
	result := 0

	for len(queue) != 0 {
		size := len(queue)
		result++
		for size > 0 {
			size--
			cur := queue[0]
			queue = queue[1:]
			for _, s := range squares {
				next := cur - s
				if next < 0 {
					break
				}
				if next == 0 {
					return result
				}
				if visited[next] {
					continue
				}
				visited[next] = true
				queue = append(queue, next)
			}
		}
	}
	return n
}

func generateSquares(n int) []int {
	squares := make([]int, 0)
	square, diff := 1, 3
	for square <= n {
		squares = append(squares, square)
		square += diff
		diff += 2
	}
	return squares
}
