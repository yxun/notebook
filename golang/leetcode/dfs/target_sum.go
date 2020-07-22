package dfs

func findTargetSumWays(nums []int, S int) int {
	return findTargetSumWaysSolve(nums, 0, S)
}

func findTargetSumWaysSolve(nums []int, start int, S int) int {
	if start == len(nums) {
		if S == 0 {
			return 1
		}
		return 0
	}
	return findTargetSumWaysSolve(nums, start+1, S+nums[start]) + findTargetSumWaysSolve(nums, start+1, S-nums[start])
}
