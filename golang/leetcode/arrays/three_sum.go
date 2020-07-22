package arrays

import "sort"

// 15. 3Sum

func threeSum(nums []int) [][]int {
	// sort
	// fix left, if it is duplicate, continue
	// move left and right, remove duplicates and process left and right
	n := len(nums)
	ret := make([][]int, 0)
	sort.Ints(nums)
	for i := 0; i < n-1; i++ {
		if i > 0 && nums[i] == nums[i-1] {
			continue
		}
		l, r := i+1, n-1
		for l < r {
			tmp := nums[i] + nums[l] + nums[r]
			if tmp == 0 {
				ret = append(ret, []int{nums[i], nums[l], nums[r]})
				l++
				r--
				for l < r && nums[l] == nums[l-1] {
					l++
				}
				for l < r && nums[r] == nums[r+1] {
					r--
				}
			} else if tmp > 0 {
				r--
			} else {
				l++
			}
		}
	}
	return ret
}
