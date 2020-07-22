package dp

// 139. Word Break

func wordBreak(s string, wordDict []string) bool {
	n := len(s)
	dp := make([]bool, n+1)
	dp[0] = true
	for i := 1; i <= n; i++ {
		for _, word := range wordDict {
			l := len(word)
			if l <= i && word == s[i-l:i] {
				dp[i] = dp[i] || dp[i-l]
			}
		}
	}
	return dp[n]
}
