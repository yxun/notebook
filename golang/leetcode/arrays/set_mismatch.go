package arrays

// 645. Set Mismatch

func findErrorNums(nums []int) []int {
	set := make(map[int]bool)
	duplicate, n := 0, len(nums)
	sum := (n * (n + 1)) / 2
	for _, i := range nums {
		if set[i] {
			duplicate = i
		}
		sum -= i
		set[i] = true
	}
	return []int{duplicate, sum + duplicate}
}
