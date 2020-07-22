package greedy

// 392. Is Subsequence
import "strings"

func isSubsequence(s, t string) bool {
	index := -1
	for _, c := range s {
		if strings.IndexRune(t[index+1:], c) == -1 {
			return false
		}
		index = strings.IndexRune(t[index+1:], c) + index + 1
	}
	return true
}
