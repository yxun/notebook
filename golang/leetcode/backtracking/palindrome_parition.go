package backtracking

// 131. Palindrome Partitioning

func partition(s string) [][]string {
	partitions := make([][]string, 0)
	temp := make([]string, 0)
	palindromTrack(s, &partitions, temp)
	return partitions
}

func palindromTrack(s string, partitions *[][]string, temp []string) {
	if len(s) == 0 {
		combo := make([]string, len(temp))
		copy(combo, temp)
		*partitions = append(*partitions, combo)
		return
	}
	for i := 0; i < len(s); i++ {
		if isPalindrome(s, 0, i) {
			temp = append(temp, s[0:i+1])
			palindromTrack(s[i+1:], partitions, temp)
			temp = temp[:len(temp)-1]
		}
	}
}

func isPalindrome(s string, begin int, end int) bool {
	for begin < end {
		if s[begin] != s[end] {
			return false
		}
		begin++
		end--
	}
	return true
}
