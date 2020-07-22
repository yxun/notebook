package backtracking

// 46. Permutations

func permute(nums []int) [][]int {
	permutes := make([][]int, 0)
	temp := make([]int, 0)
	visited := make([]bool, len(nums))
	permuteTrack(temp, &permutes, visited, nums)
	return permutes
}

func permuteTrack(temp []int, permutes *[][]int, visited []bool, nums []int) {
	if len(temp) == len(nums) {
		combo := make([]int, len(temp))
		copy(combo, temp)
		*permutes = append(*permutes, combo)
		return
	}
	for i := 0; i < len(visited); i++ {
		if visited[i] {
			continue
		}
		visited[i] = true
		temp = append(temp, nums[i])
		permuteTrack(temp, permutes, visited, nums)
		temp = temp[:len(temp)-1]
		visited[i] = false
	}
}
