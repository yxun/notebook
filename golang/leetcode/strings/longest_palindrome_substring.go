package strings

// 5. Longest Palindromic Substring

func longestPalindromeSub(s string) string {
	if len(s) == 0 {
		return s
	}
	curLen, start := 0, -1
	for i := 0; i < len(s); i++ {
		if isPalindromeSub(s, i-curLen-1, i) {
			start = i - curLen - 1
			curLen += 2
		} else if isPalindromeSub(s, i-curLen, i) {
			start = i - curLen
			curLen++
		}
	}
	return s[start : start+curLen]
}

func isPalindromeSub(s string, start, end int) bool {
	if start < 0 {
		return false
	}
	for start < end {
		if s[start] != s[end] {
			return false
		}
		start++
		end--
	}
	return true
}
