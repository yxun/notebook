package greedy

// 121. Best Time to Buy and Sell Stock

func maxProfit(prices []int) int {
	if len(prices) == 0 {
		return 0
	}
	soFarMin := prices[0]
	max := 0
	for i := 1; i < len(prices); i++ {
		if soFarMin > prices[i] {
			soFarMin = prices[i]
		} else {
			max = Max(max, prices[i]-soFarMin)
		}
	}
	return max
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
