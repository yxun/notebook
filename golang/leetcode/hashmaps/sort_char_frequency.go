package hashmaps

// 451. Sort Characters By Frequency

func frequencySort(s string) string {
	freqMap := make(map[rune]int)
	for _, c := range s {
		freqMap[c]++
	}
	freqBucket := make([][]rune, len(s)+1)
	for k, v := range freqMap {
		freqBucket[v] = append(freqBucket[v], k)
	}
	result := make([]rune, 0)
	for i := len(freqBucket) - 1; i >= 0; i-- {
		if len(freqBucket[i]) == 0 {
			continue
		}
		for _, c := range freqBucket[i] {
			for j := 0; j < i; j++ {
				result = append(result, c)
			}
		}
	}
	return string(result)
}
