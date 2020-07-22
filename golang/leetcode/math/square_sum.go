package math

// 633. Sum of Square Numbers
import "math"

func judgeSquareSum(c int) bool {
	if c < 0 {
		return false
	}
	i, j := 0, int(math.Sqrt(float64(c)))
	for i <= j {
		powSum := i*i + j*j
		if powSum == c {
			return true
		} else if powSum > c {
			j--
		} else {
			i++
		}
	}
	return false
}
