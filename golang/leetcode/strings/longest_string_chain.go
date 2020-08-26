package strings

import "sort"

// 1048. Longest String Chain

// dp
// sort words by word's length
// for each word, loop on all possible previous word with 1 letter missing
// if we have seen a previous word, update longest chain

// time sorting O(nlogn), O(ns) for loop, s string generation s <= 16
func longestStrChain(words []string) int {
	lookup := make(map[string]int)
	sort.Slice(words, func(i, j int) bool { return len(words[i]) < len(words[j]) })
	res := 0
	for _, word := range words {
		match := 0
		for i := 0; i < len(word); i++ {
			pre := word[:i] + word[i+1:]
			match = Max(match, lookup[pre]+1)
		}
		lookup[word] = match
		res = Max(res, match)
	}
	return res
}

/*
func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
*/
