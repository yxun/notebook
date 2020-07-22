package bitwise

// 693. Binary Number with Alternating Bits

func hasAlternatingBits(n int) bool {
	a := n ^ (n >> 1) // if alternating a = 1...1
	return (a & (a + 1)) == 0
}
