package strings

// 242. Valid Anagram

func isAnagram(s, t string) bool {
	cnts := make([]int, 26)
	for _, c := range s {
		cnts[c-'a']++
	}
	for _, c := range t {
		cnts[c-'a']--
	}
	for _, cnt := range cnts {
		if cnt != 0 {
			return false
		}
	}
	return true
}
