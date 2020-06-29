package backtracking

// 51. N-Queens
var (
	nQueens  [][]byte
	colUsed  []bool
	d45Used  []bool
	d135Used []bool
)

func solveNQueens(n int) [][]string {
	solutions := make([][]string, 0)
	nQueens = make([][]byte, n)
	for i := range nQueens {
		nQueens[i] = make([]byte, n)
		for j := range nQueens[i] {
			nQueens[i][j] = '.'
		}
	}
	colUsed = make([]bool, n)
	d45Used = make([]bool, 2*n-1)
	d135Used = make([]bool, 2*n-1)

	nqueensTrack(0, n, &solutions)
	return solutions
}

func nqueensTrack(row int, n int, solutions *[][]string) {
	if row == n {
		temp := make([]string, 0)
		for _, chars := range nQueens {
			temp = append(temp, string(chars))
		}
		*solutions = append(*solutions, temp)
		return
	}

	var d45Idx int
	var d135Idx int
	for col := 0; col < n; col++ {
		d45Idx = row + col
		d135Idx = n - 1 - (row - col)
		if colUsed[col] || d45Used[d45Idx] || d135Used[d135Idx] {
			continue
		}
		nQueens[row][col] = 'Q'
		colUsed[col], d45Used[d45Idx], d135Used[d135Idx] = true, true, true
		nqueensTrack(row+1, n, solutions)
		colUsed[col], d45Used[d45Idx], d135Used[d135Idx] = false, false, false
		nQueens[row][col] = '.'
	}
}
