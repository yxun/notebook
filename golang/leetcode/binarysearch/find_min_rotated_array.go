package binarysearch

// 153. Find Minimum in Rotated Sorted Array

func findMin(nums []int) int {
	l, h := 0, len(nums)-1
	var m int
	for l < h {
		m = l + (h-l)/2
		if nums[m] <= nums[h] {
			h = m
		} else {
			l = m + 1
		}
	}
	return nums[l]
}
