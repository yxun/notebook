package dp

import "math"

// 279. Perfect Squares

func numSquares(n int) int {
	squarelist := generateSquares(n)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		min := math.MaxInt32
		for _, square := range squarelist {
			if square > i {
				break
			}
			min = Min(min, dp[i-square]+1)
		}
		dp[i] = min
	}
	return dp[n]
}

func generateSquares(n int) []int {
	squares := make([]int, 0)
	square, diff := 1, 3
	for square <= n {
		squares = append(squares, square)
		square += diff
		diff += 2
	}
	return squares
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
