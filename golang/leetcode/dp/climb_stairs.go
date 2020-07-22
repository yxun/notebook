package dp

// 70. Climbing Stairs

func climbStarts(n int) int {
	// dp[i] = dp[i-1] + dp[i-2]
	if n <= 2 {
		return n
	}
	pre2, pre1 := 1, 2
	for i := 2; i < n; i++ {
		pre2, pre1 = pre1, pre1+pre2
	}
	return pre1
}
