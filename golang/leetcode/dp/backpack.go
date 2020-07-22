package dp

// backpack

func backPack(m int, A []int) int {
	// pack size m, each item size A[i]
	// dp, f[i][j]  i items and can put into size j pack or not
	// not put item i, f[i][j] = f[i-1][j]
	// put item i, if j-A[i-1] >= 0 , f[i][j] = f[i-1][j-A[i-1]]
	f := make([][]bool, len(A)+1)
	for i := 0; i <= len(A); i++ {
		f[i] = make([]bool, m+1)
	}
	f[0][0] = true
	for i := 1; i <= len(A); i++ {
		for j := 0; j <= m; j++ {
			f[i][j] = f[i-1][j]
			if j-A[i-1] >= 0 && f[i-1][j-A[i-1]] {
				f[i][j] = true
			}
		}
	}
	for i := m; i >= 0; i-- {
		if f[len(A)][i] {
			return i
		}
	}
	return 0
}
