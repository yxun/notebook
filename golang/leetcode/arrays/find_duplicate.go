package arrays

// 287. Find the Duplicate Number
type BinarySearch struct{}
type TwoPointers struct{}

func (b *BinarySearch) findDuplicate(nums []int) int {
	l, h := 1, len(nums)-1

	var mid int
	var cnt int
	for l <= h {
		mid = l + (h-l)/2
		cnt = 0
		for i := 0; i < len(nums); i++ {
			if nums[i] <= mid {
				cnt++
			}
		}
		if cnt > mid {
			h = mid - 1
		} else {
			l = mid + 1
		}
	}
	return l
}

func (t *TwoPointers) findDuplicate(nums []int) int {
	slow, fast := nums[0], nums[nums[0]]
	for slow != fast {
		slow = nums[slow]
		fast = nums[nums[fast]]
	}
	fast = 0
	for slow != fast {
		slow = nums[slow]
		fast = nums[fast]
	}
	return slow
}
