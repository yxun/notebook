package hashmaps

// 594. Longest Harmonious Subsequence

func findLHS(nums []int) int {
	countForNum := make(map[int]int)
	for _, num := range nums {
		countForNum[num]++
	}
	longest := 0
	for k := range countForNum {
		if _, ok := countForNum[k+1]; ok {
			longest = Max(longest, countForNum[k+1]+countForNum[k])
		}
	}
	return longest
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
