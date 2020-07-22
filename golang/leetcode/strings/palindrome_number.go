package strings

// 9. Palindrome Number

func isPalindromeNum(x int) bool {
	if x == 0 {
		return true
	}
	if x < 0 || x%10 == 0 {
		return false
	}
	right := 0
	for x > right {
		right = right*10 + x%10
		x /= 10
	}
	return x == right || x == right/10
}
