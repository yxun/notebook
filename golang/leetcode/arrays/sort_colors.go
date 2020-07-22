package arrays

// 75. Sort Colors

func sortColors(nums []int) {
	zi, oi, ti := -1, 0, len(nums)
	for oi < ti {
		if nums[oi] == 0 {
			zi++
			nums[zi], nums[oi] = nums[oi], nums[zi]
			oi++
		} else if nums[oi] == 2 {
			ti--
			nums[oi], nums[ti] = nums[ti], nums[oi]
		} else {
			oi++
		}
	}
}
