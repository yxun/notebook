package binarysearch

// 744. Find Smallest Letter Greater Than Target

func nextGreatestLetter(letters []byte, target byte) byte {
	n := len(letters)
	l, h := 0, n-1
	var m int
	for l <= h {
		m = l + (h-l)/2
		if letters[m] <= target {
			l = m + 1
		} else {
			h = m - 1
		}
	}
	if l < n {
		return letters[l]
	}
	return letters[0]
}
