package binarysearch

// 278. First Bad Version

func isBadVersion(version int) bool { return true }

func firstBadVersion(n int) int {
	l, h := 1, n
	var mid int
	for l < h {
		mid = l + (h-l)/2
		if isBadVersion(mid) {
			h = mid
		} else {
			l = mid + 1
		}
	}
	return l
}
