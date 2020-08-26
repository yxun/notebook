package dp

// 983. Minimum Cost For Tickets

// dp
// if no trip on day i, dp(i) = dp(i-1)
// if buy a 1-day pass, dp(i) = dp(i-1) + costs[0]
// if buy a 7-days pass, dp(i) = dp(i-7) + costs[1]
// if buy a 30 days pass, dp(i) = dp(i-30) + costs[2]

// Optimization, only look 30 days back
// time O(N), space O(N) or O(31)

func mincostTickets(days []int, costs []int) int {
	dp := make([]int, 30)
	next := 0 // next: the index of next travel day
	lastday := days[len(days)-1]

	for i := days[0]; i <= lastday; i++ {
		if i != days[next] {
			dp[i%30] = dp[(i-1)%30]
		} else {
			dp[i%30] = Min(dp[(i-1)%30]+costs[0],
				Min(dp[Max(0, i-7)%30]+costs[1],
					dp[Max(0, i-30)%30]+costs[2]))
			next++
		}
	}
	return dp[lastday%30]
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
