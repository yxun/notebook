package arrays

// 769. Max Chunks To Make Sorted

func maxChunksToSorted(arr []int) int {
	if arr == nil || len(arr) == 0 {
		return 0
	}
	ret := 0
	var right int
	right = arr[0]
	for i := 0; i < len(arr); i++ {
		right = Max(right, arr[i])
		if right == i {
			ret++
		}
	}
	return ret
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
