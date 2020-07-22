package backtracking

// 78. Subsets

func subsets(nums []int) [][]int {
	results := make([][]int, 0)
	temp := make([]int, 0)
	for size := 0; size <= len(nums); size++ {
		subsetsTrack(0, temp, &results, size, nums)
	}
	return results
}

func subsetsTrack(start int, temp []int, results *[][]int, size int, nums []int) {
	if len(temp) == size {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*results = append(*results, combo)
		return
	}
	for i := start; i < len(nums); i++ {
		temp = append(temp, nums[i])
		subsetsTrack(i+1, temp, results, size, nums)
		temp = temp[:len(temp)-1]
	}
}
