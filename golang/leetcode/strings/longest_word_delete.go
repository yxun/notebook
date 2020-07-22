package strings

import "strings"

// Longest Word in Dictionary through Deleting

func findLongestWord(s string, d []string) string {
	result := ""
	for _, target := range d {
		l1, l2 := len(result), len(target)
		if l1 > l2 || (l1 == l2 && strings.Compare(result, target) < 0) {
			continue
		}
		if isSubstr(s, target) {
			result = target
		}
	}
	return result
}

func isSubstr(s, target string) bool {
	i, j := 0, 0
	for i < len(s) && j < len(target) {
		if s[i] == target[j] {
			j++
		}
		i++
	}
	return j == len(target)
}
