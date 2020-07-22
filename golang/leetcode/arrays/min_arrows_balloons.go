package arrays

import "sort"

// 452. Minimum Number of Arrows to Burst Balloons

func findMinArrowShots(points [][]int) int {
	// similar to find non-overlapping intervals
	if len(points) == 0 {
		return 0
	}
	sort.Slice(points, func(i, j int) bool {
		return points[i][1] < points[j][1]
	})
	cnt := 1
	end := points[0][1]
	for i := 1; i < len(points); i++ {
		if points[i][0] <= end {
			continue
		}
		cnt++
		end = points[i][1]
	}
	return cnt
}
