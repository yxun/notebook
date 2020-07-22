package stackqueue

// 20. Valid Parentheses

func isValid(s string) bool {
	stack := make([]rune, 0)
	for _, c := range s {
		if c == '(' || c == '{' || c == '[' {
			stack = append(stack, c)
		} else {
			if len(stack) == 0 {
				return false
			}
			p := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			b1 := c == ')' && p != '('
			b2 := c == '}' && p != '{'
			b3 := c == ']' && p != '['
			if b1 || b2 || b3 {
				return false
			}
		}
	}
	return len(stack) == 0
}
