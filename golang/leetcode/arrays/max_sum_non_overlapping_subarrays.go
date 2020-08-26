package arrays

// 1031. Maximum Sum of Two Non-Overlapping Subarrays

// calculate preSum for each position i of A
// lMax, max sum of length L subarray
// mMax, max sum of length M subarray
// 2 cases, L is always before M, M is always before L
// sliding window to find max sum of one subarray first and then the other one

func maxSumTwoNoOverlap(A []int, L int, M int) int {
	if len(A) == 0 {
		return 0
	}

	preSum := make([]int, len(A)+1)
	for i := 0; i < len(A); i++ {
		preSum[i+1] = A[i] + preSum[i]
	}

	lMax, mMax := preSum[L], preSum[M]
	res := preSum[L+M]

	for i := L + M; i <= len(A); i++ {
		// case1: L subarray is always before M subarray
		lMax = Max(lMax, preSum[i-M]-preSum[i-M-L])
		// case2: M subarray is always before L subarray
		mMax = Max(mMax, preSum[i-L]-preSum[i-M-L])
		// compare two cases
		res = Max(res, Max(lMax+preSum[i]-preSum[i-M], mMax+preSum[i]-preSum[i-L]))
	}
	return res
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
