package strings

// 763. Partition Labels

func partitionLabels(S string) []int {
	lookup := make([]int, 26) // rune to index
	for i := 0; i < len(S); i++ {
		lookup[S[i]-'a'] = i
	}
	ret := make([]int, 0)
	firstIndex := 0
	for firstIndex < len(S) {
		lastIndex := firstIndex
		for i := firstIndex; i < len(S) && i <= lastIndex; i++ {
			index := lookup[S[i]-'a']
			if index > lastIndex {
				lastIndex = index
			}
		}
		ret = append(ret, lastIndex-firstIndex+1)
		firstIndex = lastIndex + 1
	}
	return ret
}
