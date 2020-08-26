package arrays

// 957. Prison Cells After N Days

// have a sub function nextDay() that finds the next day's cell states
// iterate and store the cell states that occurred previously
// if there's no cycle, return. if there is a cycle, break the loop and return N % cycle times

// cells fixed size of 8, we have at most 2^6 = 64 states. time and space O(1)
func prisonAfterNDays(cells []int, N int) []int {
	if len(cells) == 0 || N <= 0 {
		return cells
	}
	hasCycle := false
	cycle := 0
	lookup := make(map[string]bool)
	for i := 0; i < N; i++ {
		next := nextDay(cells)
		key := arrayToString(next)
		if _, ok := lookup[key]; !ok {
			lookup[key] = true
			cycle++
		} else {
			hasCycle = true
			break
		}
		cells = next
	}
	if hasCycle {
		N %= cycle
		for i := 0; i < N; i++ {
			cells = nextDay(cells)
		}
	}
	return cells
}

func nextDay(cells []int) []int {
	next := make([]int, len(cells))
	for i := 1; i < len(cells)-1; i++ {
		if cells[i-1] == cells[i+1] {
			next[i] = 1
		} else {
			next[i] = 0
		}
	}
	return next
}

func arrayToString(a []int) string {
	s := make([]byte, len(a))
	for i := 0; i < len(a); i++ {
		s[i] = byte(a[i])
	}
	return string(s)
}
