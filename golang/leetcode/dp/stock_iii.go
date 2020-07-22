package dp

// 123. Best Time to Buy and Sell Stock III
import "math"

func maxProfitIII(prices []int) int {
	firstBuy, firstSell := math.MinInt32, 0
	secondBuy, secondSell := math.MinInt32, 0
	for _, cur := range prices {
		if firstBuy < -cur {
			firstBuy = -cur
		}
		if firstSell < firstBuy+cur {
			firstSell = firstBuy + cur
		}
		if secondBuy < firstSell-cur {
			secondBuy = firstSell - cur
		}
		if secondSell < secondBuy+cur {
			secondSell = secondBuy + cur
		}
	}
	return secondSell
}
