package backtracking

// 77. Combinations

func combine(n int, k int) [][]int {
	combinations := make([][]int, 0)
	temp := make([]int, 0)
	combineTrack(temp, &combinations, 1, k, n)
	return combinations
}

func combineTrack(temp []int, combinations *[][]int, start int, k int, n int) {
	if k == 0 {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*combinations = append(*combinations, combo)
		return
	}
	for i := start; i <= n-k+1; i++ {
		temp = append(temp, i)
		combineTrack(temp, combinations, i+1, k-1, n)
		temp = temp[:len(temp)-1]
	}
}
