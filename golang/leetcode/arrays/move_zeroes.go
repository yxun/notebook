package arrays

// 283. Move Zeroes

func moveZeroes(nums []int) {
	if nums == nil || len(nums) == 0 {
		return
	}

	j := 0
	for i := 0; i < len(nums); i++ {
		if nums[i] != 0 {
			nums[j] = nums[i]
			j++
		}
	}
	for j < len(nums) {
		nums[j] = 0
		j++
	}
}
