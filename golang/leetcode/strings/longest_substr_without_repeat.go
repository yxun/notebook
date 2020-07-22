package strings

// 3. Longest Substring Without Repeating Characters

func lengthOfLongestSubstring(s string) int {
	if len(s) == 0 {
		return 0
	}
	win := make(map[byte]int)
	left, right := 0, 0
	ans := 1
	for right < len(s) {
		c := s[right]
		right++
		win[c]++

		for win[c] > 1 {
			d := s[left]
			left++
			win[d]--
		}
		ans = Max(right-left, ans)
	}
	return ans
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
