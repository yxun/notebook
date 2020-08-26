package arrays

// 986. Interval List Intersections

// two pointers, O(m+n)
func intervalIntersection(A [][]int, B [][]int) [][]int {
	if len(A) == 0 || len(B) == 0 {
		return [][]int{}
	}

	i, j := 0, 0
	res := make([][]int, 0)
	for i < len(A) && j < len(B) {
		a, b := A[i], B[j]

		startMax, endMin := Max(a[0], b[0]), Min(a[1], b[1])
		if endMin >= startMax {
			res = append(res, []int{startMax, endMin})
		}

		if a[1] == endMin {
			i++
		}
		if b[1] == endMin {
			j++
		}
	}
	return res
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/
