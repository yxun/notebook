package arrays

// 11. Container With Most Water

func maxArea(height []int) int {
	// S(i, j) = min(a[i],a[j]) * (j-i)
	// when a[left] < a[right], for j < right, S(left, right) > S(left, j)
	// so when a[left] < a[right], move left forward.
	// same when a[left] > a[right], move right backward
	left, right := 0, len(height)-1
	mostWater := 0
	for left <= right {
		water := (right - left) * Min(height[left], height[right])
		mostWater = Max(water, mostWater)
		if height[left] < height[right] {
			left++
		} else if height[left] > height[right] {
			right--
		} else {
			left++
			right--
		}
	}
	return mostWater
}
