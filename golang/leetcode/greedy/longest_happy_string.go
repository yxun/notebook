package greedy

// 1405. Longest Happy String

// greedy, append largest from a, b, c under conditions
func longestDiverseString(a, b, c int) string {
	res := make([]byte, 0)
	length := a + b + c
	na, nb, nc := 0, 0, 0
	for i := 0; i < length; i++ {
		if a >= b && a >= c && na != 2 || nb == 2 && a > 0 || nc == 2 && a > 0 {
			res = append(res, 'a')
			a--
			na++
			nb, nc = 0, 0
		} else if b >= a && b >= c && nb != 2 || na == 2 && b > 0 || nc == 2 && b > 0 {
			res = append(res, 'b')
			b--
			nb++
			na, nc = 0, 0
		} else if c >= a && c >= b && nc != 2 || na == 2 && c > 0 || nb == 2 && c > 0 {
			res = append(res, 'c')
			c--
			nc++
			na, nb = 0, 0
		}
	}
	return string(res)
}
