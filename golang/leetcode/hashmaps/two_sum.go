package hashmaps

// 1. Two Sum

func twoSum(nums []int, target int) []int {
	index := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		if _, ok := index[target-nums[i]]; ok {
			return []int{index[target-nums[i]], i}
		} else {
			index[nums[i]] = i
		}
	}
	return nil
}
