package backtracking

// 37. Sudoku Solver
var (
	rowsUsed  [][]bool
	colsUsed  [][]bool
	cubesUsed [][]bool
)

func solveSudoku(board [][]byte) {
	rowsUsed, colsUsed, cubesUsed = make([][]bool, 9), make([][]bool, 9), make([][]bool, 9)
	for i := range rowsUsed {
		rowsUsed[i], colsUsed[i], cubesUsed[i] = make([]bool, 10), make([]bool, 10), make([]bool, 10)
	}

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}
			num := int(board[i][j] - '0')
			rowsUsed[i][num] = true
			colsUsed[j][num] = true
			cubesUsed[cubeNum(i, j)][num] = true
		}
	}

	sudokuTrack(0, 0, board)
}

func sudokuTrack(row int, col int, board [][]byte) bool {
	for row < 9 && board[row][col] != '.' {
		if col == 8 {
			row = row + 1
			col = 0
		} else {
			col = col + 1
		}
	}
	if row == 9 {
		return true
	}

	for num := 1; num <= 9; num++ {
		if rowsUsed[row][num] || colsUsed[col][num] || cubesUsed[cubeNum(row, col)][num] {
			continue
		}
		rowsUsed[row][num], colsUsed[col][num], cubesUsed[cubeNum(row, col)][num] = true, true, true
		board[row][col] = byte(num + '0')
		if sudokuTrack(row, col, board) {
			return true
		}
		board[row][col] = '.'
		rowsUsed[row][num], colsUsed[col][num], cubesUsed[cubeNum(row, col)][num] = false, false, false
	}
	return false
}

func cubeNum(i, j int) int {
	r, c := i/3, j/3
	return r*3 + c
}
