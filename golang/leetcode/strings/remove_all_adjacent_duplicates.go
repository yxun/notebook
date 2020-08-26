package strings

// 1047. Remove All Adjacent Duplicates In String

// Use Stack
func removeDuplicates(S string) string {
	stack := make([]rune, 0)
	for _, r := range S {
		if len(stack) != 0 && stack[len(stack)-1] == r {
			stack = stack[:len(stack)-1] // pop
		} else {
			stack = append(stack, r)
		}
	}
	return string(stack)
}
