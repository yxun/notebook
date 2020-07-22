package hashmaps

// 347. Top K Frequent Elements

func topKFrequent(nums []int, k int) []int {
	freqMap := make(map[int]int)
	for _, num := range nums {
		freqMap[num]++
	}
	buckets := make([][]int, len(nums)+1)
	for key, v := range freqMap {
		buckets[v] = append(buckets[v], key)
	}
	topk := make([]int, 0)
	for i := len(buckets) - 1; i >= 0; i-- {
		if len(buckets[i]) == 0 {
			continue
		}
		if len(buckets[i]) <= k-len(topk) {
			topk = append(topk, buckets[i]...)
		} else {
			topk = append(topk, buckets[i][:(k-len(topk))]...)
		}

	}
	return topk
}
