package binarysearch

// 34. Find First and Last Position of Element in Sorted Array

func searchRange(nums []int, target int) []int {
	first, last := findFirst(nums, target), findFirst(nums, target+1)-1
	if first == len(nums) || nums[first] != target {
		return []int{-1, -1}
	}
	return []int{first, Max(first, last)}
}

func findFirst(nums []int, target int) int {
	l, h := 0, len(nums)
	var m int
	for l < h {
		m = l + (h-l)/2
		if nums[m] >= target {
			h = m
		} else {
			l = m + 1
		}
	}
	return l
}

// Max returns larger int
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
