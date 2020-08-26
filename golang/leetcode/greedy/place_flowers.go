package greedy

// 605. Can Place Flowers

func canPlaceFlowers(flowerbed []int, n int) bool {
	cnt := 0
	pre, next := 0, 0
	for i := 0; i < len(flowerbed) && cnt < n; i++ {
		if flowerbed[i] == 1 {
			continue
		}
		if i == 0 {
			pre = 0
		} else {
			pre = flowerbed[i-1]
		}
		if i == len(flowerbed)-1 {
			next = 0
		} else {
			next = flowerbed[i+1]
		}
		if pre == 0 && next == 0 {
			flowerbed[i] = 1
			cnt++
		}
	}
	return cnt >= n
}
