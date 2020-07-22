package strings

// 205. Isomorphic Strings

func isIsomorphic(s, t string) bool {
	preIndexS, preIndexT := make([]int, 256), make([]int, 256)
	for i := 0; i < len(s); i++ {
		sc, tc := s[i], t[i]
		if preIndexS[sc] != preIndexT[tc] {
			return false
		}
		preIndexS[sc], preIndexT[tc] = i+1, i+1

	}
	return true
}
