package dp

import "sort"

// 377. Combination Sum IV

func combinationSum4(nums []int, target int) int {
	if len(nums) == 0 {
		return 0
	}
	dp := make([]int, target+1)
	dp[0] = 1
	sort.Ints(nums)
	for i := 1; i <= target; i++ {
		for j := 0; j < len(nums) && nums[j] <= i; j++ {
			dp[i] += dp[i-nums[j]]
		}
	}
	return dp[target]
}
