package dp

// 198. House Robber

func rob(nums []int) int {
	// dp[i] = max(dp[i-2] + nums[i], dp[i-1])
	pre2, pre1 := 0, 0
	for i := 0; i < len(nums); i++ {
		cur := Max(pre2+nums[i], pre1)
		pre2, pre1 = pre1, cur
	}
	return pre1
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
