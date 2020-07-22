package dp

// 413. Arithmetic Slices

func numberOfArithmeticSlices(A []int) int {
	// when A[i] - A[i-1] == A[i-1] - A[i-2], dp[i] = dp[i-1] + 1
	if len(A) == 0 {
		return 0
	}
	n := len(A)
	dp := make([]int, n)
	for i := 2; i < n; i++ {
		if A[i]-A[i-1] == A[i-1]-A[i-2] {
			dp[i] = dp[i-1] + 1
		}
	}
	total := 0
	for _, cnt := range dp {
		total += cnt
	}
	return total
}
