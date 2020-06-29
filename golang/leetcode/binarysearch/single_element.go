package binarysearch

// 540. Single Element in a Sorted Array

func singleNonDuplicate(nums []int) int {
	l, h := 0, len(nums)-1
	var m int
	for l < h {
		m = l + (h-l)/2
		if m%2 == 1 {
			m-- // make m be an even index
		}
		if nums[m] == nums[m+1] {
			l = m + 2
		} else {
			h = m
		}
	}
	return nums[l]
}
