package examples

import "fmt"

type Direction int

const (
	North Direction = iota
	East
	South
	West
)

func (d Direction) String() string {
	return [...]string{"North", "East", "South", "West"}[d]
}

func TestEnum() {
	var d Direction = North
	fmt.Print(d)
	switch d {
	case North:
		fmt.Println(" goes up ")
	case South:
		fmt.Println(" goes down ")
	default:
		fmt.Println(" stays put ")
	}
}
