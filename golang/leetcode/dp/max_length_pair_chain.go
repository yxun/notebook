package dp

import "sort"

// 646. Maximum Length of Pair Chain

func findLongestChain(pairs [][]int) int {
	if len(pairs) == 0 {
		return 0
	}
	sort.Slice(pairs, func(i, j int) bool { return pairs[i][0] < pairs[j][0] })
	n := len(pairs)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = 1
	}

	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if pairs[j][1] < pairs[i][0] {
				dp[i] = Max(dp[i], dp[j]+1)
			}
		}
	}
	ret := 0
	for i := 0; i < n; i++ {
		ret = Max(ret, dp[i])
	}
	return ret
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
