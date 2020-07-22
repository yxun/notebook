package greedy

import "sort"

// 406. Queue Reconstruction by Height

func reconstructQueue(people [][]int) [][]int {
	// insert higher people first, h des, k inc
	if len(people) == 0 || len(people[0]) == 0 {
		return [][]int{}
	}
	sort.Slice(people, func(i, j int) bool {
		if people[i][0] == people[j][0] {
			return people[i][1] < people[j][1]
		} else {
			return people[i][0] > people[j][0]
		}
	})
	ret := make([][]int, len(people))
	for _, p := range people {
		// insert p in slice, index < len(people)
		index := p[1]
		copy(ret[index+1:], ret[index:])
		ret[index] = p
	}
	return ret
}
