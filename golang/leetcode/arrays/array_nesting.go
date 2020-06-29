package arrays

// 565. Array Nesting
func arrayNesting(nums []int) int {
	max := 0
	for i := 0; i < len(nums); i++ {
		cnt := 0
		var t int
		for j := i; nums[j] != -1; {
			cnt++
			t = nums[j]
			nums[j] = -1 // mark visited
			j = t
		}
		max = Max(max, cnt)
	}
	return max
}

// Max compares two int values and returns the larger one
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
