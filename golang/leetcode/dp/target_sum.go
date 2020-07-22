package dp

// 494. Target Sum
// P +, N -
// sum(P) - sum(N) = target
// sum(P) - sum(N) + sum(N) + sum(P) = target + sum(P) + sum(N)
// 2 * sum(P) = target + sum(nums)

func findTargetSumWays(nums []int, S int) int {
	sum := computeArraySum(nums)
	if sum < S || (sum+S)%2 == 1 {
		return 0
	}
	W := (sum + S) / 2
	dp := make([]int, W+1)
	dp[0] = 1
	for _, num := range nums {
		for i := W; i >= num; i-- {
			dp[i] = dp[i] + dp[i-num]
		}
	}
	return dp[W]
}

/*
func computeArraySum(nums []int) int {
	sum := 0
	for _, num := range nums {
		sum += num
	}
	return sum
}
*/
