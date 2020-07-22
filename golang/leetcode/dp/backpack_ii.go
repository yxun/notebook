package dp

// backpack ii
// n items, pack size m, size A[], value V[]

func backPackII(m int, A []int, V []int) int {
	// f[i][j] from i items , pack size j, max value
	// not put item i, f[i][j] = f[i-1][j]
	// put item i, f[i][j] = f[i-1][j-A[i]] + V[i]
	f := make([][]int, len(A)+1)
	for i := range f {
		f[i] = make([]int, m+1)
	}
	for i := 1; i <= len(A); i++ {
		for j := 0; j <= m; j++ {
			f[i][j] = f[i-1][j]
			if j-A[i-1] >= 0 {
				f[i][j] = Max(f[i-1][j], f[i-1][j-A[i-1]]+V[i-1])
			}
		}
	}
	return f[len(A)][m]
}
