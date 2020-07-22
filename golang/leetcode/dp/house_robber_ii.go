package dp

// 213. House Robber II

func robII(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	n := len(nums)
	if n == 1 {
		return nums[0]
	}
	return Max(rob2(nums, 0, n-2), rob2(nums, 1, n-1))
}

func rob2(nums []int, first int, last int) int {
	// dp[i] = max(dp[i-2] + nums[i], dp[i-1])
	pre2, pre1 := 0, 0
	for i := first; i <= last; i++ {
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
