package bfs

// 127. Word Ladder

func ladderLength(beginWord string, endWord string, wordList []string) int {
	wordList = append(wordList, beginWord)
	N := len(wordList)
	start, end := N-1, 0
	for end < N && wordList[end] != endWord {
		end++
	}
	if end == N {
		return 0
	}
	graph := buildGraph(wordList)
	return getShortestPath(graph, start, end)
}

func buildGraph(wordList []string) [][]int {
	N := len(wordList)
	graph := make([][]int, N)
	for i := 0; i < N; i++ {
		graph[i] = make([]int, 0)
		for j := 0; j < N; j++ {
			if isConnect(wordList[i], wordList[j]) {
				graph[i] = append(graph[i], j)
			}
		}
	}
	return graph
}

func isConnect(s1, s2 string) bool {
	diffCnt := 0
	for i := 0; i < len(s1) && diffCnt <= 1; i++ {
		if s1[i] != s2[i] {
			diffCnt++
		}
	}
	return diffCnt == 1
}

func getShortestPath(graph [][]int, start int, end int) int {
	queue := make([]int, 0)
	visited := make([]bool, len(graph))
	queue = append(queue, start)
	visited[start] = true
	result := 0

	for len(queue) != 0 {
		size := len(queue)
		result++
		for i := 0; i < size; i++ {
			cur := queue[0]
			queue = queue[1:]
			for _, next := range graph[cur] {
				if next == end {
					return result + 1
				}
				if visited[next] {
					continue
				}
				visited[next] = true
				queue = append(queue, next)
			}
		}
	}
	return 0
}
