package arrays

// 667. Beautiful Arrangement II

func constructArray(n int, k int) []int {
	ret := make([]int, n)
	ret[0] = 1
	for i, interval := 1, k; i <= k; i, interval = i+1, interval-1 {
		if i%2 == 1 {
			ret[i] = ret[i-1] + interval
		} else {
			ret[i] = ret[i-1] - interval
		}
	}
	for i := k + 1; i < n; i++ {
		ret[i] = i + 1
	}
	return ret
}
