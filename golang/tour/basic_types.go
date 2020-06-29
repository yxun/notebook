package main

import (
	"fmt"
	"math"
	"math/bits"
)

var (
	boo  bool
	s    string
	i    int  // int, int8, int16, int32, int64
	ui   uint // uint, uint8, uint16, uint32, uint64, uintptr
	b    byte // alias for uint8
	r    rune // alias for int32, represents a Unicode code point
	f32  float32
	f64  float64
	c64  complex64
	c128 complex128
)

func basicTypes() {
	fmt.Printf("Type: %T Value: %v\n", boo, boo)
	fmt.Printf("Type: %T Value: %v\n", s, s)
	fmt.Printf("Type: %T Value: %v\n", i, i)
	fmt.Printf("Type: %T Value: %v\n", ui, ui)
	fmt.Printf("Type: %T Value: %v\n", b, b)
	fmt.Printf("Type: %T Value: %v\n", r, r)
	fmt.Printf("Type: %T Value: %v\n", f32, f32)
	fmt.Printf("Type: %T Value: %v\n", f64, f64)
	fmt.Printf("Type: %T Value: %v\n", c64, c64)
	fmt.Printf("Type: %T Value: %v\n", c128, c128)

	fmt.Printf("MinInt32: %d\n", math.MinInt32)
	fmt.Printf("MaxInt32: %d\n", math.MaxInt32)
	fmt.Printf("MinInt64: %d\n", math.MinInt64)
	fmt.Printf("MaxInt64: %d\n", math.MaxInt64)
	fmt.Printf("MaxUint32: %d\n", math.MaxUint32)
	fmt.Printf("MaxUint64: %d\n", uint64(math.MaxUint64)) // math constants by default are interpreted as int. Need to explicitly assign the uint64 type.

	fmt.Println()
	var uint64Max uint64 = (1 << bits.UintSize) - 1
	var i64Max uint64 = (1<<bits.UintSize)/2 - 1
	var i64Min int64 = (1 << bits.UintSize) / -2
	fmt.Printf("MaxUint64: %d\n", uint64Max)
	fmt.Printf("MaxInt64: %d\n", i64Max)
	fmt.Printf("MinInt64: %d\n", i64Min)
}
