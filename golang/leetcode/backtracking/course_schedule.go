package backtracking

// 207. Course Schedule

func canFinish(numCourses int, prerequisites [][]int) bool {
	graphic := make([][]int, numCourses)
	for _, pre := range prerequisites {
		graphic[pre[0]] = append(graphic[pre[0]], pre[1])
	}
	globalMarked := make([]bool, numCourses)
	localMarked := make([]bool, numCourses)
	for i := 0; i < numCourses; i++ {
		if hasCycle(globalMarked, localMarked, graphic, i) {
			return false
		}
	}
	return true
}

// backtracking
func hasCycle(globalMarked []bool, localMarked []bool, graphic [][]int, cur int) bool {
	if localMarked[cur] {
		return true
	}
	if globalMarked[cur] {
		return false
	}
	globalMarked[cur] = true
	localMarked[cur] = true
	for _, next := range graphic[cur] {
		if hasCycle(globalMarked, localMarked, graphic, next) {
			return true
		}
	}
	localMarked[cur] = false
	return false
}
