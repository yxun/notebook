package dp

// 322. Coin Change

func coinChange(coins []int, amount int) int {
	if amount == 0 {
		return 0
	}
	dp := make([]int, amount+1)
	for _, coin := range coins {
		for i := coin; i <= amount; i++ {
			if i == coin {
				dp[i] = 1
			} else if dp[i] == 0 && dp[i-coin] != 0 {
				dp[i] = dp[i-coin] + 1
			} else if dp[i-coin] != 0 {
				dp[i] = Min(dp[i], dp[i-coin]+1)
			}
		}
	}
	if dp[amount] == 0 {
		return -1
	}
	return dp[amount]
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
