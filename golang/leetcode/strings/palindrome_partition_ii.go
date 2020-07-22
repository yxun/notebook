package strings

// 132. Palindrome Partitioning II

func minCut(s string) int {
	// dp, f[i] min cut from 0 to i
	// f[i] = Min(f[i], f[j]+1), last cut
	// init f[i] = i-1
	if len(s) == 0 || len(s) == 1 {
		return 0
	}
	f := make([]int, len(s)+1)
	f[0] = -1
	f[1] = 0
	for i := 1; i <= len(s); i++ {
		f[i] = i - 1
		for j := 0; j < i; j++ {
			if isPalindrome(s, j, i-1) {
				f[i] = Min(f[i], f[j]+1)
			}
		}
	}
	return f[len(s)]
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

/*
func isPalindrome(s string, i, j int) bool {
	for i < j {
		if s[i] != s[j] {
			return false
		}
		i++
		j--
	}
	return true
}
*/
