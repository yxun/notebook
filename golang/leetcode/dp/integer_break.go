package dp

// 343. Integer Break

func integerBreak(n int) int {
	dp := make([]int, n+1)
	dp[1] = 1
	for i := 2; i <= n; i++ {
		for j := 1; j <= i-1; j++ {
			dp[i] = Max(dp[i], Max(j*dp[i-j], j*(i-j)))
		}
	}
	return dp[n]
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
