package arrays

// 969. Pancake Sorting

// find the index i of the next maximum number x
// reverse i+1 numbers, so that the x will be at A[0]
// reverse x numbers, so that x will be at A[x-1]
// repeat
// time O(N^2)

func pancakeSort(A []int) []int {
	res := make([]int, 0)
	largest := len(A)
	for i := 0; i < len(A); i++ {
		index := findLargest(A, largest)
		flip(A[:index+1])
		flip(A[:largest])
		res = append(res, index+1)
		res = append(res, largest)
		largest--
	}
	return res
}

func findLargest(A []int, target int) int {
	for i := 0; i < len(A); i++ {
		if A[i] == target {
			return i
		}
	}
	return -1
}

func flip(sub []int) {
	for i, j := 0, len(sub)-1; i < j; i, j = i+1, j-1 {
		sub[i], sub[j] = sub[j], sub[i]
	}
}
