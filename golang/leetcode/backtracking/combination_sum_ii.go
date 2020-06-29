package backtracking

import "sort"

// 40. Combination Sum II

func combinationSum2(candidates []int, target int) [][]int {
	combinations := make([][]int, 0)
	sort.Ints(candidates)
	temp := make([]int, 0)
	visited := make([]bool, len(candidates))
	comboTrack2(temp, &combinations, visited, 0, target, candidates)
	return combinations
}

func comboTrack2(temp []int, combinations *[][]int, hasVisited []bool, start int, target int, candidates []int) {
	if target == 0 {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*combinations = append(*combinations, combo)
		return
	}

	for i := start; i < len(candidates); i++ {
		if i != 0 && candidates[i] == candidates[i-1] && !hasVisited[i-1] {
			continue
		}
		if candidates[i] <= target {
			temp = append(temp, candidates[i])
			hasVisited[i] = true
			comboTrack2(temp, combinations, hasVisited, i+1, target-candidates[i], candidates)
			hasVisited[i] = false
			temp = temp[:len(temp)-1]
		}
	}
}
