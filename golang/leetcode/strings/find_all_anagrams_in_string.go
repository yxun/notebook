package strings

// 438. Find All Anagrams in a String

func findAnagrams(s, p string) []int {
	win := make(map[byte]int)
	need := make(map[byte]int)
	for i := 0; i < len(p); i++ {
		need[p[i]]++
	}
	left, right, match := 0, 0, 0
	ans := make([]int, 0)
	for right < len(s) {
		c := s[right]
		right++
		if need[c] != 0 {
			win[c]++
			if win[c] == need[c] {
				match++
			}
		}
		for right-left >= len(p) {
			if right-left == len(p) && match == len(need) {
				ans = append(ans, left)
			}
			d := s[left]
			left++
			if need[d] != 0 {
				if win[d] == need[d] {
					match--
				}
				win[d]--
			}
		}
	}
	return ans
}
