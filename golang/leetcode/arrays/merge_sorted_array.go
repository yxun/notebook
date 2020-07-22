package arrays

// 88. Merge Sorted Array

func merge(nums1, nums2 []int, m, n int) {
	index1, index2 := m-1, n-1
	indexMerge := m + n - 1
	for index1 >= 0 || index2 >= 0 {
		if index1 < 0 {
			nums1[indexMerge] = nums2[index2]
			indexMerge, index2 = indexMerge-1, index2-1
		} else if index2 < 0 {
			nums1[indexMerge] = nums1[index1]
			indexMerge, index1 = indexMerge-1, index1-1
		} else if nums1[index1] > nums2[index2] {
			nums1[indexMerge] = nums1[index1]
			indexMerge, index1 = indexMerge-1, index1-1
		} else {
			nums1[indexMerge] = nums2[index2]
			indexMerge, index2 = indexMerge-1, index2-1
		}
	}
}
