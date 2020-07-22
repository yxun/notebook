package backtracking

import "sort"

// 47. Permutations II

func permuteUnique(nums []int) [][]int {
	permutes := make([][]int, 0)
	temp := make([]int, 0)
	sort.Ints(nums)
	visited := make([]bool, len(nums))
	permuteTrack2(temp, &permutes, visited, nums)
	return permutes
}

func permuteTrack2(temp []int, permutes *[][]int, visited []bool, nums []int) {
	if len(temp) == len(nums) {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*permutes = append(*permutes, combo)
		return
	}
	for i := 0; i < len(visited); i++ {
		if i != 0 && nums[i] == nums[i-1] && !visited[i-1] {
			continue // avoid adding repeated elements
		}
		if visited[i] {
			continue
		}
		visited[i] = true
		temp = append(temp, nums[i])
		permuteTrack2(temp, permutes, visited, nums)
		temp = temp[:len(temp)-1]
		visited[i] = false
	}
}
