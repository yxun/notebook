package strings

import "math"

// 76. Minimum Window Substring

func minWindow(s, t string) string {
	win := make(map[byte]int)
	need := make(map[byte]int)
	for i := 0; i < len(t); i++ {
		need[t[i]]++
	}
	left, right := 0, 0
	match, start, end := 0, 0, 0
	min := math.MaxInt64
	var c byte
	for right < len(s) {
		c = s[right]
		right++
		if need[c] != 0 {
			win[c]++
			if win[c] == need[c] {
				match++
			}
		}

		for match == len(need) {
			if right-left < min {
				min = right - left
				start, end = left, right
			}
			c = s[left]
			left++
			if need[c] != 0 {
				if win[c] == need[c] {
					match--
				}
				win[c]--
			}
		}
	}
	if min == math.MaxInt64 {
		return ""
	}
	return s[start:end]
}
