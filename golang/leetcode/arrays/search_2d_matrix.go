package arrays

// 74. Search a 2D Matrix

func searchMatrix(matrix [][]int, target int) bool {
	// binary search
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}

	row, col := len(matrix), len(matrix[0])
	l, r := 0, row-1
	for l <= r {
		midRow := l + (r-l)/2
		if matrix[midRow][0] <= target && target <= matrix[midRow][len(matrix[midRow])-1] {
			m, n := 0, col-1
			for m <= n {
				midCol := m + (n-m)/2
				if matrix[midRow][midCol] == target {
					return true
				} else if matrix[midRow][midCol] < target {
					m = midCol + 1
				} else {
					n = midCol - 1
				}
			}
			return false
		} else if matrix[midRow][0] > target {
			r = midRow - 1
		} else {
			l = midRow + 1
		}
	}
	return false
}
