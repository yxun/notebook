package dp

// 583. Delete Operation for Two Strings

func minDistance(word1, word2 string) int {
	// similar as longest common subsequence
	// find lcs and then min deletion = m + n - 2 * lcs
	m, n := len(word1), len(word2)
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}
	for i := 1; i <= m; i++ {
		for j := 1; j <= n; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1] + 1
			} else {
				dp[i][j] = Max(dp[i][j-1], dp[i-1][j])
			}
		}
	}
	return m + n - 2*dp[m][n]
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
