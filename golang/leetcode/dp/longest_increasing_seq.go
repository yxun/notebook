package dp

// 300. Longest Increasing Subsequence

func lengthOfLIS(nums []int) int {
	// dp[n] = max{1, dp[i] + 1 | s[i] < s[n] && i < n }
	// time O(N^2)
	n := len(nums)
	dp := make([]int, n)
	for i := 0; i < n; i++ {
		max := 1
		for j := 0; j < i; j++ {
			if nums[i] > nums[j] {
				max = Max(max, dp[j]+1)
			}
		}
		dp[i] = max
	}
	result := 0
	for i := 0; i < n; i++ {
		result = Max(result, dp[i])
	}
	return result
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/

// binary search O(nlogn)
