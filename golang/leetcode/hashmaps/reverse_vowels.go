package hashmaps

// 345. Reverse Vowels of a String

func reverseVowels(s string) string {
	vowels := map[byte]bool{'a': true, 'e': true, 'i': true, 'o': true, 'u': true,
		'A': true, 'E': true, 'I': true, 'O': true, 'U': true}

	if len(s) == 0 {
		return s
	}
	i, j := 0, len(s)-1
	result := make([]byte, len(s))
	for i <= j {
		ci, cj := s[i], s[j]
		if _, ok := vowels[ci]; !ok {
			result[i] = ci
			i++
		} else if _, ok := vowels[cj]; !ok {
			result[j] = cj
			j--
		} else {
			result[i] = cj
			i++
			result[j] = ci
			j--
		}
	}
	return string(result)
}
