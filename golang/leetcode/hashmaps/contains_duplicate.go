package hashmaps

// 217. Contains Duplicate

func containsDuplicate(nums []int) bool {
	set := make(map[int]bool)
	for _, num := range nums {
		set[num] = true
	}
	return len(set) < len(nums)
}
