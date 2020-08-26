package slidingwindow

// 1248. Count Number of Nice Subarrays

// sliding window, fix i and move j first, when k odd numbers, fix j and move i, count subarrays
// time O(N), space O(1)

// similar questions
// 992. Subarrays with K Different Integers
// 1358 Number of Substrings Containing All Three Characters
// 1248 Count Number of Nice Subarrays
// 1234 Replace the Substring for Balanced String
// 1004 Max Consecutive Ones III
// 930 Binary Subarrays With Sum
// 992 Subarrays with K Different Integers
// 904 Fruit Into Baskets
// 862 Shortest Subarray with Sum at Least K
// 209 Minimum Size Subarray Sum

func numberOfSubarrays(nums []int, k int) int {
	res := 0
	left := 0
	count := 0
	for right := 0; right < len(nums); right++ {
		if nums[right]%2 == 1 {
			k--
			count = 0
		}
		for k == 0 {
			k += nums[left] & 1
			left++
			count++
		}
		res += count
	}
	return res
}
