package arrays

// 4. Median of Two Sorted Arrays

func findMedianSortedArrays(nums1, nums2 []int) float64 {
	n := len(nums1) + len(nums2)
	if n%2 == 1 {
		return float64(findKth(nums1, nums2, n/2+1))
	} else {
		small := findKth(nums1, nums2, n/2)
		big := findKth(nums1, nums2, n/2+1)
		return float64((small + big)) / 2.0
	}
}

// kth in 0 index array a, a[k-1]

// time O(n), space O(m+n)
func findKthEasy(nums1, nums2 []int, k int) int {
	m, n := len(nums1), len(nums2)
	merge := make([]int, m+n)
	i, j, d := 0, 0, 0
	for i < m && j < n {
		if nums1[i] < nums2[j] {
			merge[d] = nums1[i]
			d++
			i++
		} else {
			merge[d] = nums2[j]
			d++
			j++
		}
	}
	for i < m {
		merge[d] = nums1[i]
		d++
		i++
	}
	for j < n {
		merge[d] = nums2[j]
		d++
		j++
	}
	return merge[k-1]
}

// divide and conquer approach 1
// compare the middle elements of nums1 and nums2
// time O(logm + logn)
func findKth(nums1, nums2 []int, k int) int {
	if len(nums1) == 0 {
		return nums2[k-1]
	}
	if len(nums2) == 0 {
		return nums1[k-1]
	}
	m, n := len(nums1), len(nums2)
	mid1, mid2 := m/2, n/2

	if mid1+mid2 < k-1 {
		if nums1[mid1] > nums2[mid2] {
			return findKth(nums1, nums2[mid2+1:], k-mid2-1)
		} else {
			return findKth(nums1[mid1+1:], nums2, k-mid1-1)
		}
	} else {
		if nums1[mid1] > nums2[mid2] {
			return findKth(nums1[:mid1], nums2, k)
		} else {
			return findKth(nums1, nums2[:mid2], k)
		}
	}
}

// divide and conquer approach 2
// instead of dividing arrays into n/2 and m/2 then recursing, we can divide them both by k/2 then recursing
// if x[k/2] == y[k/2] return
// if x[k/2] < y[k/2] find in x[k/2:] and y[:k/2]
// else find in x[:k/2] and y[k/2:]
// time O(logk)
