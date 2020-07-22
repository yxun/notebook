package arrays

// 42. Trapping Rain Water

func trap(height []int) int {
	l, r := 0, len(height)-1
	water, minHeight := 0, 0
	for l < r {
		minHeight = Min(height[l], height[r])
		for l < r && height[l] <= minHeight {
			water += minHeight - height[l]
			l++
		}
		for l < r && height[r] <= minHeight {
			water += minHeight - height[r]
			r--
		}
	}
	return water
}
