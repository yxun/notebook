package strings

// 647. Palindromic Substrings

func countSubstrings(s string) int {
	cnt := 0
	for i := 0; i < len(s); i++ {
		extendSubstrings(s, i, i, &cnt)
		extendSubstrings(s, i, i+1, &cnt)
	}
	return cnt
}

func extendSubstrings(s string, start, end int, cnt *int) {
	for start >= 0 && end < len(s) && s[start] == s[end] {
		start--
		end++
		*cnt++
	}
}
