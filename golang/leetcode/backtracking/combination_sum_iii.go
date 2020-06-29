package backtracking

// 216. Combination Sum III

func combinationSum3(k int, n int) [][]int {
	combinations := make([][]int, 0)
	temp := make([]int, 0)
	comboTrack3(k, n, 1, temp, &combinations)
	return combinations
}

func comboTrack3(k int, n int, start int, temp []int, combinations *[][]int) {
	if k == 0 && n == 0 {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*combinations = append(*combinations, combo)
		return
	}
	if k == 0 || n == 0 {
		return
	}
	for i := start; i <= 9; i++ {
		temp = append(temp, i)
		comboTrack3(k-1, n-i, i+1, temp, combinations)
		temp = temp[:len(temp)-1]
	}
}
