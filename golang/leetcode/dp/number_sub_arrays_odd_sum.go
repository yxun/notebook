package dp

// 1524. Number of Sub-arrays With Odd Sum

// odd[i] the number of subarray ending at arr[i] that has odd sum
// even[i] the number of subarray ending at arr[i] that has even sum
// if arr[i+1] is odd, odd[i+1] = even[i] + 1, even[i+1] = odd[i]
// if arr[i+1] is even, odd[i+1] = odd[i], even[i+1] = even[i] + 1
// only required the previous value in odd and even

// time O(n), space O(1)

import "math"

func numOfSubarrays(arr []int) int {
	res, odd, even := 0, 0, 0
	mod := int(math.Pow(10, 9) + 7)

	for i := 0; i < len(arr); i++ {
		if arr[i]%2 == 1 {
			odd, even = even+1, odd
		} else {
			even = even + 1
		}
		res = (res + odd) % mod
	}
	return res
}
