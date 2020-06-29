package arrays

// 766. Toeplitz Matrix

func isToeplitzMatrix(matrix [][]int) bool {
	for i := 0; i < len(matrix[0]); i++ {
		if !check(matrix, matrix[0][i], 0, i) {
			return false
		}
	}
	for i := 0; i < len(matrix); i++ {
		if !check(matrix, matrix[i][0], i, 0) {
			return false
		}
	}
	return true
}

func check(matrix [][]int, expectValue int, row int, col int) bool {
	if row >= len(matrix) || col >= len(matrix[0]) {
		return true
	}
	if matrix[row][col] != expectValue {
		return false
	}
	return check(matrix, expectValue, row+1, col+1)
}
