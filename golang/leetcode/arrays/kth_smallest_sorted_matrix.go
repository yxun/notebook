package arrays

import "container/heap"

// 378. Kth Smallest Element in a Sorted Matrix

// bs

func (b *BinarySearch) kthSmallest(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	l, h := matrix[0][0], matrix[m-1][n-1]

	var mid int
	var cnt int
	for l <= h {
		mid = l + (h-l)/2
		cnt = 0
		for i := 0; i < m; i++ {
			for j := 0; j < n && matrix[i][j] <= mid; j++ {
				cnt++
			}
		}
		if cnt < k {
			l = mid + 1
		} else {
			h = mid - 1
		}
	}
	return l
}

// heap
type Heap struct{}

type Tuple struct {
	x   int
	y   int
	val int
}

type PriorityQueue []*Tuple

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
	return pq[i].val < pq[j].val
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Tuple)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil
	*pq = old[0 : n-1]
	return item
}

func (h *Heap) kthSmallest(matrix [][]int, k int) int {
	m, n := len(matrix), len(matrix[0])
	pq := make(PriorityQueue, n)
	for j := 0; j < n; j++ {
		pq[j] = &Tuple{
			x:   0,
			y:   j,
			val: matrix[0][j],
		}
	}
	heap.Init(&pq)

	for i := 0; i < k-1; i++ {
		t := heap.Pop(&pq).(*Tuple)
		if t.x == m-1 {
			continue
		}
		heap.Push(&pq, &Tuple{
			x:   t.x + 1,
			y:   t.y,
			val: matrix[t.x+1][t.y],
		})
	}
	return heap.Pop(&pq).(*Tuple).val
}
