package arrays

// 1262. Greatest Sum Divisible by Three

// dp
// if sum % 3 == 0 return sum
// if sum % 3 == 1 remove the smallest number n which has n % 3 == 1
// if sum % 3 == 2 remove the smallest number n which has n % 3 == 2

import "math"

func maxSumDivThree(nums []int) int {
	res, leftOne, leftTwo := 0, math.MaxInt32, math.MaxInt32
	for _, n := range nums {
		res += n
		if n%3 == 1 {
			leftTwo = Min(leftTwo, leftOne+n)
			leftOne = Min(leftOne, n)
		}
		if n%3 == 2 {
			leftOne = Min(leftOne, leftTwo+n)
			leftTwo = Min(leftTwo, n)
		}
	}

	if res%3 == 0 {
		return res
	} else if res%3 == 1 {
		return res - leftOne
	} else {
		return res - leftTwo
	}
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/

// dp for k problem

func maxSumDivK(nums []int, k int) int {
	if k == 0 {
		return -1
	}
	dp := make([]int, k)
	for _, n := range nums {
		tmp := make([]int, k)
		copy(tmp, dp)
		for i := 0; i < k; i++ {
			dp[(n+tmp[i])%k] = Max(dp[(n+tmp[i])%k], n+tmp[i])
		}
	}
	return dp[0]
}
