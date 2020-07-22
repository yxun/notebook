package binarysearch

// optional
// 300. Longest Increasing Subsequence
// if tails[i-1] < x <= tails[i], update tails[i] = x
func lengthOfLTS(nums []int) int {
	n := len(nums)
	tails := make([]int, n)
	length := 0
	for _, num := range nums {
		index := bsLIS(tails, length, num)
		tails[index] = num
		if index == length {
			length++
		}
	}
	return length
}

func bsLIS(tails []int, length int, key int) int {
	l, h := 0, length
	for l < h {
		mid := l + (h-l)/2
		if tails[mid] == key {
			return mid
		} else if tails[mid] > key {
			h = mid
		} else {
			l = mid + 1
		}
	}
	return l
}
