package strings

// 1513. Number of Substrings With Only 1s

// count the current number of consecutive "1"
// for each new element
// there will be more count substring with all 1s

// time O(N), space O(1)

import "math"

func numSub(s string) int {
	res, count := 0, 0
	mod := int(math.Pow(10, 9) + 7)
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			count++
		} else {
			count = 0
		}
		res = (res + count) % mod
	}
	return res
}
