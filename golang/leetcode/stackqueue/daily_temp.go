package stackqueue

// 739. Daily Temperatures

func dailyTemperatures(T []int) []int {
	ret := make([]int, len(T))
	stack := make([]int, 0)
	for cur := 0; cur < len(T); cur++ {
		for len(stack) != 0 && T[cur] > T[stack[len(stack)-1]] {
			pre := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			ret[pre] = cur - pre
		}
		stack = append(stack, cur)
	}
	return ret
}
