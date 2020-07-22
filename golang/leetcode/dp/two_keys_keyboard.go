package dp

// 650. 2 Keys Keyboard

import "math"

func minStepsRecur(n int) int {
	if n == 1 {
		return 0
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return i + minStepsRecur(n/i)
		}
	}
	return n
}

func minStepsDP(n int) int {
	dp := make([]int, n+1)
	h := int(math.Sqrt(float64(n)))
	for i := 2; i <= n; i++ {
		dp[i] = i
		for j := 2; j <= h; j++ {
			if i%j == 0 {
				dp[i] = dp[j] + dp[i/j]
				break
			}
		}
	}
	return dp[n]
}
