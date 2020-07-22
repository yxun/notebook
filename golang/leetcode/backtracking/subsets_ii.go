package backtracking

import "sort"

// 90. Subsets II

func subsetsWithDup(nums []int) [][]int {
	sort.Ints(nums)
	results := make([][]int, 0)
	temp := make([]int, 0)
	visited := make([]bool, len(nums))
	for size := 0; size <= len(nums); size++ {
		subsetsTrack2(0, temp, &results, visited, size, nums)
	}
	return results
}

func subsetsTrack2(start int, temp []int, results *[][]int, visited []bool, size int, nums []int) {
	if len(temp) == size {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*results = append(*results, combo)
		return
	}
	for i := start; i < len(nums); i++ {
		if i != 0 && nums[i] == nums[i-1] && !visited[i-1] {
			continue
		}
		temp = append(temp, nums[i])
		visited[i] = true
		subsetsTrack2(i+1, temp, results, visited, size, nums)
		visited[i] = false
		temp = temp[:len(temp)-1]
	}
}
