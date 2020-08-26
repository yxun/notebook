package strings

// 1328. Break a Palindrome

// check half of the string

func breakPalindrome(palindrome string) string {
	s := []byte(palindrome)
	for i := 0; i < len(s)/2; i++ {
		if s[i] != 'a' {
			s[i] = 'a'
			return string(s)
		}
	}
	// if all 'a'
	s[len(s)-1] = 'b'
	if len(s) < 2 {
		return ""
	}
	return string(s)
}
