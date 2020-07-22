package stackqueue

// 503. Next Greater Element II

func nextGreaterElements(nums []int) []int {
	ret := make([]int, len(nums))
	for i := 0; i < len(nums); i++ {
		ret[i] = -1
	}
	stack := make([]int, 0)
	for i := 0; i < len(nums)*2; i++ {
		num := nums[i%len(nums)]
		for len(stack) != 0 && num > nums[stack[len(stack)-1]] {
			ret[stack[len(stack)-1]] = num
			stack = stack[:len(stack)-1]
		}
		if i < len(nums) {
			stack = append(stack, i)
		}
	}
	return ret
}
