package binarysearch

// 69. Implement int sqrt(int x)

func mySqrt(x int) int {
	if x <= 1 {
		return x
	}
	l, h := 1, x

	var mid int
	var sqrt int
	for l <= h {
		mid = l + (h-l)/2
		sqrt = x / mid
		if sqrt == mid {
			return mid
		} else if mid > sqrt {
			h = mid - 1
		} else {
			l = mid + 1
		}
	}
	return h
}
