package arrays

import "sort"

// 945. Minimum Increment to Make Array Unique

// sort the array
// the current number need to be at least prev + 1
// time O(NlogN), space O(1)
func minIncrementForUnique(A []int) int {
	sort.Ints(A)
	res, need := 0, 0
	for _, a := range A {
		res += Max(need-a, 0)
		need = Max(a, need) + 1
	}
	return res
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
