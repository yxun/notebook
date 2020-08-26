package slidingwindow

// 1358. Number of Substrings Containing All Three Characters

func numberOfSubstrings(s string) int {
	na, nb, nc := 0, 0, 0
	res := 0
	left := 0
	for right := 0; right < len(s); right++ {
		if s[right] == 'a' {
			na++
		} else if s[right] == 'b' {
			nb++
		} else if s[right] == 'c' {
			nc++
		}
		for na > 0 && nb > 0 && nc > 0 {
			if s[left] == 'a' {
				na--
			} else if s[left] == 'b' {
				nb--
			} else if s[left] == 'c' {
				nc--
			}
			left++
		}
		res += left
	}
	return res
}
