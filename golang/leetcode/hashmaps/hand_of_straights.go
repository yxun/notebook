package hashmaps

import "sort"

// 846. Hand of Straights

// time O(MlogM + MW), where M is the number of different cards
func isNStraightHand(hand []int, W int) bool {
	cards := make(map[int]int)
	for _, c := range hand {
		cards[c]++
	}

	// because map iteration is randomized, sort keys first
	keys := make([]int, 0, len(cards))
	for k := range cards {
		keys = append(keys, k)
	}
	sort.Ints(keys)

	for _, k := range keys {
		if cards[k] > 0 {
			for i := W - 1; i >= 0; i-- {
				if cards[k+i] < cards[k] {
					return false
				}
				cards[k+i] -= cards[k]
			}
		}
	}
	return true
}
