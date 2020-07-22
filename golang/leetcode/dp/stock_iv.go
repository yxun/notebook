package dp

// 188. Best Time to Buy and Sell Stock IV

func maxProfitIV(k int, prices []int) int {
	n := len(prices)
	if k >= n/2 {
		maxProfit := 0
		for i := 1; i < n; i++ {
			if prices[i] > prices[i-1] {
				maxProfit += prices[i] - prices[i-1]
			}
		}
		return maxProfit
	}

	maxProfit := make([][]int, k+1)
	for i := range maxProfit {
		maxProfit[i] = make([]int, n)
	}
	for i := 1; i <= k; i++ {
		localMax := maxProfit[i-1][0] - prices[0]
		for j := i; j < n; j++ {
			maxProfit[i][j] = Max(maxProfit[i][j-1], prices[j]+localMax)
			localMax = Max(localMax, maxProfit[i-1][j]-prices[j])
		}
	}
	return maxProfit[k][n-1]
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
