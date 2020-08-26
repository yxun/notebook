package stackqueue

// 946. Validate Stack Sequences

// time, space O(n)
// keep pushing pushed elements into stack if the top element on the stack is different from the current one of popped
// keep poping out of the top element from stack if it is same as the current one of popped
// check if the stack is empty

func validateStackSequences(pushed []int, popped []int) bool {

	stack := make([]int, 0)
	popindex := 0
	for _, item := range pushed {
		stack = append(stack, item)
		for len(stack) != 0 && stack[len(stack)-1] == popped[popindex] {
			stack = stack[:len(stack)-1]
			popindex++
		}
	}
	return len(stack) == 0
}
