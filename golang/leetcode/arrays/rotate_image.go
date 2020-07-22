package arrays

// 48. Rotate Image

func rotate(matrix [][]int) {
	// 1. up side down rotate [i][:] --> [n-1-i][:]
	// 2. diagonal rotate: [i][j] --> [j][i]

	n := len(matrix)
	// up side down
	for i := 0; i < n/2; i++ {
		matrix[i], matrix[n-1-i] = matrix[n-1-i], matrix[i]
	}

	// diagonal rotate
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		}
	}
}

func rotate2(matrix [][]int) {
	// rotate four points together
	// [x][y] --> [n-1-x][y] --> [y][n-1-x] --> [n-1-y][x]
	n := len(matrix)
	for i := 0; i < n/2; i++ {
		for j := 0; j < n-n/2; j++ {

			matrix[i][j], matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i] =
				matrix[n-1-j][i], matrix[n-1-i][n-1-j], matrix[j][n-1-i], matrix[i][j]
		}
	}
}

/*
Python zip
def rotate(matrix):
    matrix[:] = zip(*matrix[::-1])

*/
