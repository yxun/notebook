package arrays

// 240. Search a 2D Matrix II

func searchMatrix2(matrix [][]int, target int) bool {
	if matrix == nil || len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	m, n := len(matrix), len(matrix[0])
	row, col := 0, n-1
	for row < m && col >= 0 {
		if target == matrix[row][col] {
			return true
		} else if target < matrix[row][col] {
			col--
		} else {
			row++
		}
	}
	return false
}
