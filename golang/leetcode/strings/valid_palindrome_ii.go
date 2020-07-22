package strings

// 680. Valid Palindrome II

func validPalindrome(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return isPalindrome(s, i, j-1) || isPalindrome(s, i+1, j)
		}
	}
	return true
}

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
