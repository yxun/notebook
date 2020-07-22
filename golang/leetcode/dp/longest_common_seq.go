package dp

// 1143. Longest Common Subsequence

func lcs(text1, text2 string) int {
	// when s1[i] == s2[j], dp[i][j] = dp[i-1][j-1] + 1
	// when s1[i] != s2[j], dp[i][j] = Max(dp[i-1][j], dp[i][j-1])
	n1, n2 := len(text1), len(text2)
	dp := make([][]int, n1+1)
	for i := range dp {
		dp[i] = make([]int, n2+1)
	}

	for i := 1; i <= n1; i++ {
		for j := 1; j <= n2; j++ {
			if text1[i-1] == text2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = Max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[n1][n2]
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
