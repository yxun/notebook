package strings

// 567. Permutation in String

func checkInclusion(s1, s2 string) bool {
	win := make(map[byte]int)
	need := make(map[byte]int)
	for i := 0; i < len(s1); i++ {
		need[s1[i]]++
	}
	left, right, match := 0, 0, 0
	for right < len(s2) {
		c := s2[right]
		right++
		if need[c] != 0 {
			win[c]++
			if win[c] == need[c] {
				match++
			}
		}

		for right-left >= len(s1) {
			if match == len(need) {
				return true
			}
			d := s2[left]
			left++
			if need[d] != 0 {
				if win[d] == need[d] {
					match--
				}
				win[d]--
			}
		}
	}
	return false
}
