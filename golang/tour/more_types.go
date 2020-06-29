package main

import (
	"fmt"
	"math"
	"strings"
)

type VertexI struct {
	X int
	Y int
}

type VertexF struct {
	Lat, Long float64
}

func pointers() {
	i, j := 42, 2701

	p := &i
	fmt.Println(*p)
	*p = 21
	fmt.Println(i)

	p = &j
	*p = *p / 37
	fmt.Println(j)
}

func arrays() {
	var a [2]string
	a[0] = "Hello"
	a[1] = "World"
	fmt.Println(a[0], a[1])
	fmt.Println(a)

	primes := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes)

	// Slices []T
	var s []int = primes[1:4]
	fmt.Println(s)

	// length and capacity
	s = []int{2, 3, 5, 7, 11, 13}
	printSlice(s)
	s = s[:0]
	printSlice(s)
	s = s[:4]
	printSlice(s)
	s = s[2:]
	printSlice(s)

	// The zero value of a slice is nil. A nil slice has length and capacity 0

	// create dynamically-sized arrays with make function
	// make allocates a zeroed array and returns a slice
	// make([]int, length, capacity)

	// append(slice, value)
	// range form of the for loop iterates over a slice or map
	var pow = []int{1, 2, 4, 8}
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}

func ticTacToe() {
	board := [][]string{
		[]string{"-", "-", "-"},
		[]string{"-", "-", "-"},
		[]string{"-", "-", "-"},
	}

	board[0][0] = "X"
	board[2][2] = "O"
	board[1][2] = "X"
	board[1][0] = "O"
	board[0][2] = "X"

	for i := 0; i < len(board); i++ {
		fmt.Printf("%s\n", strings.Join(board[i], " "))
	}
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func maps() {
	// the zero value of a map is nil. A nil map has no keys, nor can keys be added
	// make function returns a map the given type
	var m map[string]VertexF
	m = make(map[string]VertexF)
	m["Bell Labs"] = VertexF{
		40.68433, -74.39967,
	}
	fmt.Println(m["Bell Labs"])

	m = map[string]VertexF{
		"Google": VertexF{
			37.422, -122.08,
		},
	}
	fmt.Println(m)

	n := make(map[string]int)

	n["Answer"] = 42
	fmt.Println("The value: ", n["Answer"])
	delete(m, "Answer")
	fmt.Println("The value: ", n["Answer"])

	v, ok := m["Answer"]
	fmt.Println("The value:", v, "Present?", ok)
}

// Functions values as function arguments and return values
func compute(fn func(float64, float64) float64) float64 {
	return fn(3, 4)
}

// closures
func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func moreTypes() {
	v := VertexI{1, 2}
	v.X = 4
	fmt.Println(v.X)

	p := &v
	p.X = 1e9
	fmt.Println(v)

	pointers()
	arrays()
	ticTacToe()
	maps()

	hypot := func(x, y float64) float64 {
		return math.Sqrt(x*x + y*y)
	}
	fmt.Println(hypot(5, 12))
	fmt.Println(compute(hypot))
	fmt.Println(compute(math.Pow))

	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
