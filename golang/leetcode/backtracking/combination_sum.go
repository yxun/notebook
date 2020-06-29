package backtracking

// 39. Combination Sum

func combinationSum(candidates []int, target int) [][]int {
	combinations := make([][]int, 0)
	temp := make([]int, 0)
	comboTrack(temp, &combinations, 0, target, candidates)
	return combinations
}

func comboTrack(temp []int, combinations *[][]int, start int, target int, candidates []int) {
	if target == 0 {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*combinations = append(*combinations, combo)
		return
	}
	for i := start; i < len(candidates); i++ {
		if candidates[i] <= target {
			temp = append(temp, candidates[i])
			comboTrack(temp, combinations, i, target-candidates[i], candidates)
			temp = temp[:len(temp)-1]
		}
	}
}
