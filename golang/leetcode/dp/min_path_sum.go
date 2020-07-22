package dp

// 64. Minimum Path Sum

func minPathSum(grid [][]int) int {
	if len(grid) == 0 {
		return 0
	}
	m, n := len(grid), len(grid[0])
	dp := make([]int, n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if j == 0 {
				dp[j] = dp[j] // from upper to current
			} else if i == 0 {
				dp[j] = dp[j-1] // from left to current
			} else {
				dp[j] = Min(dp[j-1], dp[j])
			}
			dp[j] += grid[i][j]
		}
	}
	return dp[n-1]
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
