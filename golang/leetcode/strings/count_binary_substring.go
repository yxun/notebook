package strings

// 696. Count Binary Substrings

func countBinarySubstring(s string) int {
	preLen, curLen, count := 0, 1, 0
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			curLen++
		} else {
			preLen = curLen
			curLen = 1
		}

		if preLen >= curLen {
			count++
		}
	}
	return count
}
