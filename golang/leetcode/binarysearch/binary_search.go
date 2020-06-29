package binarysearch

func binarySearch(nums []int, key int) int {
	l, h := 0, len(nums)-1
	var m int
	for l <= h {
		m = l + (h-l)/2
		if nums[m] == key {
			return m
		} else if nums[m] > key {
			h = m - 1
		} else {
			l = m + 1
		}
	}
	return -1
}
