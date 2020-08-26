package slidingwindow

// 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

// sliding window problems
// 1425 Constrained Subsequence Sum
// 1358 Number of Substrings Containing All Three Characters
// 1248 Count Number of Nice Subarrays
// 1234 Replace the Substring for Balanced String
// 1004 Max Consecutive Ones III
// 930 Binary Subarrays With Sum
// 992 Subarrays with K Different Integers
// 904 Fruit Into Baskets
// 862 Shortest Subarray with Sum at Least K
// 209 Minimum Size Subarray Sum

// Absolute difference between min and max elements of subarray
// find the longest subarray for every right pointer (iterate it) by shrinking left pointer
// left = 0, right --> i, and then use right-- to find new left, 0 <-- right, left = right+1
// java deque

import "math"

func longestSubarray(nums []int, limit int) int {
	if len(nums) == 0 {
		return 0
	}
	left := 0
	min, max := nums[0], nums[0]
	res := 0

	for i := 0; i < len(nums); i++ {
		diff := FloatMax(math.Abs(float64(nums[i]-min)), math.Abs(float64(max-nums[i])))
		if int(diff) <= limit {
			min, max = IntMin(nums[i], min), IntMax(nums[i], max)
			res = IntMax(res, i-left+1)
		} else {
			right := i - 1
			min, max = nums[i], nums[i]
			for left < right && int(math.Abs(float64(nums[i]-nums[right]))) <= limit {
				min, max = IntMin(nums[right], min), IntMax(nums[right], max)
				right--
			}
			left = right + 1
		}
	}
	return res
}

func FloatMax(x, y float64) float64 {
	if x > y {
		return x
	}
	return y
}

func IntMax(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func IntMin(x, y int) int {
	if x < y {
		return x
	}
	return y
}
