package dp

// 376. Wiggle Subsequence

func wiggleMaxLength(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	up, down := 1, 1
	for i := 1; i < len(nums); i++ {
		if nums[i] > nums[i-1] {
			up = down + 1
		} else if nums[i] < nums[i-1] {
			down = up + 1
		}
	}
	return Max(up, down)
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
