package backtracking

// 79. Word Search
var (
	direction [][]int
	m         int
	n         int
)

func exist(board [][]byte, word string) bool {
	direction = [][]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	if len(word) == 0 {
		return true
	}
	if board == nil || len(board) == 0 || len(board[0]) == 0 {
		return false
	}

	m, n = len(board), len(board[0])
	visited := make([][]bool, m)
	for i := range visited {
		visited[i] = make([]bool, n)
	}

	for r := 0; r < m; r++ {
		for c := 0; c < n; c++ {
			if wordTrack(0, r, c, visited, board, word) {
				return true
			}
		}
	}
	return false
}

func wordTrack(curLen int, r int, c int, visited [][]bool, board [][]byte, word string) bool {
	if curLen == len(word) {
		return true
	}
	if r < 0 || r >= m || c < 0 || c >= n || board[r][c] != word[curLen] || visited[r][c] {
		return false
	}

	visited[r][c] = true

	for _, d := range direction {
		if wordTrack(curLen+1, r+d[0], c+d[1], visited, board, word) {
			return true
		}
	}
	visited[r][c] = false
	return false
}
