package dp

// 45. Jump Game II

func jump(nums []int) int {
	// dp, f[i] min steps from 0 to i
	// f[i] = min(f[j]+1, f[i]), f[i] max value f[i] = i
	f := make([]int, len(nums))
	// init f[0] = 0
	f[0] = 0
	for i := 1; i < len(nums); i++ {
		// set max steps of f[i] = i
		f[i] = i
		for j := 0; j < i; j++ {
			if nums[j]+j >= i {
				f[i] = Min(f[j]+1, f[i])
			}
		}
	}
	return f[len(nums)-1]
}

/*
func Min(x, y int) int {
	if x < y {
		return x
	}
	return y
}
*/

func jump2(nums []int) int {
	// greedy, assume you can always reach the last index
	curEnd, curFarthest, step := 0, 0, 0
	for i := 0; i < len(nums)-1; i++ {
		curFarthest = Max(curFarthest, i+nums[i])
		if curFarthest >= len(nums)-1 {
			step++
			break
		}
		// local max end
		if i == curEnd {
			curEnd = curFarthest
			step++
		}
	}
	return step
}
