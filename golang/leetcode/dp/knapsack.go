package dp

func knapsack(W int, N int, weights []int, values []int) int {
	// put item i into pack, dp[i][j] = dp[i-1][j-w] + v
	// not put item i, dp[i][j] = dp[i-1][j]
	// dp[i][j] = Max(dp[i-1][j], dp[i-1][j-w]+v)

	dp := make([][]int, N+1)
	for i := range dp {
		dp[i] = make([]int, W+1)
	}
	for i := 1; i <= N; i++ {
		w, v := weights[i-1], values[i-1]
		for j := 1; j <= W; j++ {
			if j >= w {
				dp[i][j] = Max(dp[i-1][j], dp[i-1][j-w]+v)
			} else {
				dp[i][j] = dp[i-1][j]
			}
		}
	}
	return dp[N][W]
}

// space optimization
// dp[j] = Max(dp[j], dp[j-w] + v)

func knapsack2(W int, N int, weights []int, values []int) int {
	dp := make([]int, W+1)
	for i := 1; i <= N; i++ {
		w, v := weights[i-1], values[i-1]
		for j := W; j >= 1; j-- {
			if j >= w {
				dp[j] = Max(dp[j], dp[j-w]+v)
			}
		}
	}
	return dp[W]
}
