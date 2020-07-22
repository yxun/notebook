package dfs

// 130. Surrounded Regions
/*
var (
	directions [][]int
	m          int
	n          int
)
*/

func solve(board [][]byte) {
	directions = [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	if len(board) == 0 {
		return
	}
	m, n = len(board), len(board[0])

	for i := 0; i < m; i++ {
		regionTrack(board, i, 0)
		regionTrack(board, i, n-1)
	}
	for i := 0; i < n; i++ {
		regionTrack(board, 0, i)
		regionTrack(board, m-1, i)
	}

	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if board[i][j] == 'T' {
				board[i][j] = 'O'
			} else if board[i][j] == 'O' {
				board[i][j] = 'X'
			}
		}
	}
}

func regionTrack(board [][]byte, r int, c int) {
	if r < 0 || r >= m || c < 0 || c >= n || board[r][c] != 'O' {
		return
	}
	board[r][c] = 'T'
	for _, d := range directions {
		regionTrack(board, r+d[0], c+d[1])
	}
}
