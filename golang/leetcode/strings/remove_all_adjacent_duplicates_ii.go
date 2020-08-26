package strings

// 1209. Remove All Adjacent Duplicates in String II

// Use Stack
func removeDuplicatesII(s string, k int) string {
	stack := make([]*Tuple, 0)
	res := make([]rune, 0)
	for _, r := range s {
		if len(stack) != 0 && stack[len(stack)-1].r == r {
			stack[len(stack)-1].count++
		} else {
			stack = append(stack, &Tuple{r: r, count: 1})
		}
		if stack[len(stack)-1].count == k {
			stack = stack[:len(stack)-1]
		}
	}
	for _, t := range stack {
		for i := 0; i < t.count; i++ {
			res = append(res, t.r)
		}
	}
	return string(res)
}

type Tuple struct {
	r     rune
	count int
}
