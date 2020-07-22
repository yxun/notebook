package arrays

// 167. Two Sum II - Input array is sorted

func twoSum(numbers []int, target int) []int {
	if len(numbers) == 0 {
		return nil
	}
	i, j := 0, len(numbers)-1
	for i < j {
		sum := numbers[i] + numbers[j]
		if sum == target {
			return []int{i + 1, j + 1}
		} else if sum < target {
			i++
		} else {
			j--
		}
	}
	return nil
}
