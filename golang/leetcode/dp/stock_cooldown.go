package dp

// 309. Best Time to Buy and Sell Stock with Cooldown

func maxProfitCooldown(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	n := len(prices)
	buy, s1, sell, s2 := make([]int, n), make([]int, n), make([]int, n), make([]int, n)
	s1[0], buy[0] = -prices[0], -prices[0]
	sell[0], s2[0] = 0, 0
	for i := 1; i < n; i++ {
		buy[i] = s2[i-1] - prices[i]
		s1[i] = Max(buy[i], s1[i-1])
		sell[i] = Max(buy[i], s1[i-1]) + prices[i]
		s2[i] = Max(s2[i-1], sell[i-1])
	}
	return Max(sell[n-1], s2[n-1])
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
