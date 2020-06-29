package arrays

// 485. Max Consecutive Ones

func findMaxConsecutiveOnes(nums []int) int {
	max, cur := 0, 0
	for _, n := range nums {
		if n == 0 {
			cur = 0
		} else {
			cur = cur + 1
		}
		max = Max(max, cur)
	}
	return max
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
