package backtracking

import "sort"

// 698. Partition to K Equal Sum Subsets

func canPartitionKSubsets(nums []int, k int) bool {
	if k > len(nums) {
		return false
	}
	sum := 0
	for _, n := range nums {
		sum += n
	}
	if sum%k != 0 {
		return false
	}
	visited := make([]bool, len(nums))
	sort.Ints(nums)
	return dfsPartK(nums, 0, len(nums)-1, visited, sum/k, k)
}

func dfsPartK(nums []int, sum int, start int, visited []bool, target int, round int) bool {
	if round == 0 {
		return true
	}
	if sum == target && dfsPartK(nums, 0, len(nums)-1, visited, target, round-1) {
		return true
	}
	for i := start; i >= 0; i-- {
		if !visited[i] && sum+nums[i] <= target {
			visited[i] = true
			if dfsPartK(nums, sum+nums[i], i-1, visited, target, round) {
				return true
			}
			visited[i] = false
		}
	}
	return false
}
