package backtracking

// 210. Course Schedule II

func findOrder(numCourses int, prerequisites [][]int) []int {
	graphic := make([][]int, numCourses)
	for _, pre := range prerequisites {
		graphic[pre[0]] = append(graphic[pre[0]], pre[1])
	}
	ret := make([]int, 0)
	globalMarked := make([]bool, numCourses)
	localMarked := make([]bool, numCourses)
	for i := 0; i < numCourses; i++ {
		if hasCycle2(globalMarked, localMarked, graphic, i, &ret) {
			return []int{}
		}
	}
	return ret
}

func hasCycle2(globalMarked []bool, localMarked []bool, graphic [][]int, cur int, ret *[]int) bool {
	if localMarked[cur] {
		return true
	}
	if globalMarked[cur] {
		return false
	}
	globalMarked[cur] = true
	localMarked[cur] = true
	for _, next := range graphic[cur] {
		if hasCycle2(globalMarked, localMarked, graphic, next, ret) {
			return true
		}
	}
	localMarked[cur] = false
	*ret = append(*ret, cur)
	return false
}
