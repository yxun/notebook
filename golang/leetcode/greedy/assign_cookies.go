package greedy

import "sort"

// 455. Assign Cookies
// local optimal to global optimal

func findContentChildren(g, s []int) int {
	if len(g) == 0 || len(s) == 0 {
		return 0
	}
	sort.Ints(g)
	sort.Ints(s)
	gi, si := 0, 0
	for gi < len(g) && si < len(s) {
		if g[gi] <= s[si] {
			gi++
		}
		si++
	}
	return gi
}
