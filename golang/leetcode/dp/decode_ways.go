package dp

// 91. Decode Ways
import "strconv"

func numDecodings(s string) int {
	if len(s) == 0 {
		return 0
	}
	n := len(s)
	dp := make([]int, n+1)
	dp[0] = 1
	if s[0] == '0' {
		dp[1] = 0
	} else {
		dp[1] = 1
	}

	for i := 2; i <= n; i++ {
		one, _ := strconv.Atoi(s[i-1 : i])
		if one != 0 {
			dp[i] += dp[i-1]
		}
		if s[i-2] == '0' {
			continue
		}
		two, _ := strconv.Atoi(s[i-2 : i])
		if two <= 26 {
			dp[i] += dp[i-2]
		}
	}
	return dp[n]
}
