package arrays

// 697. Degree of an Array

func findShortestSubArray(nums []int) int {
	numsCnt := make(map[int]int)
	numsLastIndex := make(map[int]int)
	numsFirstIndex := make(map[int]int)

	var num int
	var cnt int
	var ok bool

	for i := 0; i < len(nums); i++ {
		num = nums[i]
		cnt, ok = numsCnt[num]
		if ok {
			numsCnt[num] = cnt + 1
		} else {
			numsCnt[num] = 1
		}
		numsLastIndex[num] = i
		_, ok = numsFirstIndex[num]
		if !ok {
			numsFirstIndex[num] = i
		}
	}
	maxCnt := 0
	for _, num := range nums {
		maxCnt = Max(maxCnt, numsCnt[num])
	}

	ret := len(nums)
	for i := 0; i < len(nums); i++ {
		num = nums[i]
		cnt = numsCnt[num]
		if cnt != maxCnt {
			continue
		}
		ret = Min(ret, numsLastIndex[num]-numsFirstIndex[num]+1)
	}
	return ret
}

/*
func Max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
*/

// Min compares two int values and returns the smaller one
func Min(a, b int) int {
	if a < b {
		return a
	}
	return b
}
