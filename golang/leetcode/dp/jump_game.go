package dp

// 55. Jump Game

func canJump(nums []int) bool {
	// dp, f[i] means can jump from 0 to i
	// f[i] = f[j] && j+nums[j] >= i, think last jump
	if len(nums) == 0 {
		return true
	}
	f := make([]bool, len(nums))
	f[0] = true
	for i := 1; i < len(nums); i++ {
		for j := 0; j < i; j++ {
			if f[j] && j+nums[j] >= i {
				f[i] = true
			}
		}
	}
	return f[len(nums)-1]
}

func canJump2(nums []int) bool {
	// greedy, count each local max reach
	if len(nums) == 0 || len(nums) == 1 {
		return true
	}

	idx, reach := 0, 0
	for idx < len(nums)-1 && idx <= reach {
		reach = Max(reach, idx+nums[idx])
		idx++
	}
	return reach >= len(nums)-1
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
