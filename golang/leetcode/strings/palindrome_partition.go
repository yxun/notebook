package strings

// 131. Palindrome Partitioning

func partition(s string) [][]string {
	// backtracking
	ret := make([][]string, 0)
	if len(s) == 0 {
		return ret
	}
	temp := make([]string, 0)
	checkPart(s, temp, &ret)
	return ret
}

func checkPart(s string, temp []string, ret *[][]string) {
	if len(s) == 0 {
		list := make([]string, len(temp))
		copy(list, temp)
		*ret = append(*ret, list)
		return
	}
	for i := 0; i < len(s); i++ {
		if isPalin(s[0 : i+1]) {
			temp = append(temp, s[0:i+1])
			checkPart(s[i+1:], temp, ret)
			temp = temp[:len(temp)-1]
		}
	}
}

func isPalin(s string) bool {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		if s[i] != s[j] {
			return false
		}
	}
	return true
}
