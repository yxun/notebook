package strings

// 409. Longest Palindrome

func longestPalindrome(s string) int {
	cnts := make([]int, 256)
	for _, c := range s {
		cnts[c]++
	}
	result := 0
	for _, cnt := range cnts {
		result += (cnt / 2) * 2
	}
	if result < len(s) {
		result++
	}
	return result
}
