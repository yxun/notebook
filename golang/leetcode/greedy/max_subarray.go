package greedy

// 53. Maximum Subarray

func maxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	preSum := nums[0]
	maxSum := preSum
	for i := 1; i < len(nums); i++ {
		if preSum > 0 {
			preSum += nums[i]
		} else {
			preSum = nums[i]
		}
		maxSum = Max(maxSum, preSum)
	}
	return maxSum
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
