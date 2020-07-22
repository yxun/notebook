package greedy

// 122. Best Time to Buy and Sell Stock II

func maxProfitII(prices []int) int {
	ret := 0
	for i := 1; i < len(prices); i++ {
		if prices[i] > prices[i-1] {
			ret += (prices[i] - prices[i-1])
		}
	}
	return ret
}
