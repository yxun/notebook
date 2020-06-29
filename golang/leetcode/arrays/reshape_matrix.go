package arrays

// 566. Reshape the Matrix

func matrixReshape(nums [][]int, r int, c int) [][]int {
	if nums == nil || len(nums) == 0 {
		return nil
	}
	i, j := len(nums), len(nums[0])
	if i*j != r*c {
		return nums
	}

	res := make([][]int, r)
	for i := range res {
		res[i] = make([]int, c)
	}
	m, n := 0, 0
	for _, row := range nums {
		for _, num := range row {
			if n < c {
				res[m][n] = num
				n++
			} else {
				n = 0
				m++
				res[m][n] = num
				n++
			}
		}
	}
	return res
}
