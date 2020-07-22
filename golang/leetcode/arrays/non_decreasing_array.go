package arrays

// 665. Non-decreasing Array

func checkPossibility(nums []int) bool {
	cnt := 0
	for i := 1; i < len(nums) && cnt < 2; i++ {
		if nums[i] >= nums[i-1] {
			continue
		}
		cnt++
		if i-2 >= 0 && nums[i-2] > nums[i] {
			nums[i] = nums[i-1]
		} else {
			nums[i-1] = nums[i]
		}
	}
	return cnt <= 1
}
