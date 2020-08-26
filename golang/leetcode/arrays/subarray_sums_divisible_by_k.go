package arrays

// 974. Subarray Sums Divisible by K

// if sum[0:i] % K == sum[0:j] % K, sum[i+1:j] is divisible by K
// need to find out how many index i has the same mod of K
func subarrayDivByK(A []int, K int) int {
	lookup := make([]int, K)
	lookup[0] = 1
	count, sum := 0, 0
	for _, a := range A {
		sum = (sum + a) % K
		if sum < 0 {
			sum += K
		}
		count += lookup[sum]
		lookup[sum]++
	}
	return count
}
