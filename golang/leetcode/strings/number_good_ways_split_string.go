package strings

// 1525. Number of Good Ways to Split a String

// sliding window

func numSplits(s string) int {
	rc, lc := make([]int, 26), make([]int, 26)
	r, l := 0, 0
	res := 0
	for _, c := range s {
		if rc[c-'a'] == 0 {
			r++
		}
		rc[c-'a']++
	}

	for _, c := range s {
		if lc[c-'a'] == 0 {
			l++
		}
		lc[c-'a']++

		if rc[c-'a'] == 1 {
			r--
		}
		rc[c-'a']--

		if l == r {
			res++
		}
	}
	return res
}
