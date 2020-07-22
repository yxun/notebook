package hashmaps

// 128. Longest Consecutive Sequence

func longestConsecutive(nums []int) int {
	countForNum := make(map[int]int)
	for _, num := range nums {
		countForNum[num] = 1
	}
	for _, num := range nums {
		forward(countForNum, num)
	}
	return maxCount(countForNum)
}

func forward(countForNum map[int]int, num int) int {
	if _, ok := countForNum[num]; !ok {
		return 0
	}
	cnt := countForNum[num]
	if cnt > 1 {
		return cnt
	}
	cnt = forward(countForNum, num+1) + 1
	countForNum[num] = cnt
	return cnt
}

func maxCount(countForNum map[int]int) int {
	max := 0
	for k, _ := range countForNum {
		max = Max(max, countForNum[k])
	}
	return max
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
