package stackqueue

// 636. Exclusive Time of Functions

import (
	"strconv"
	"strings"
)

func exclusiveTime(n int, logs []string) []int {
	res := make([]int, n)
	stack := make([]int, 0)
	pre := 0
	for _, l := range logs {
		id, _ := strconv.Atoi(strings.Split(l, ":")[0])
		status := strings.Split(l, ":")[1]
		time, _ := strconv.Atoi(strings.Split(l, ":")[2])

		if status == "start" {
			if len(stack) != 0 {
				fid := stack[len(stack)-1]
				res[fid] += time - pre
			}
			stack = append(stack, id)
			pre = time
		} else if status == "end" {
			fid := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[fid] += time - pre + 1
			pre = time + 1
		}
	}
	return res
}
