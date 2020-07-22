package strings

// 49. Group Anagrams
import "sort"

type sortRunes []rune

func (s sortRunes) Len() int {
	return len(s)
}

func (s sortRunes) Less(i, j int) bool {
	return s[i] < s[j]
}

func (s sortRunes) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func SortString(s string) string {
	r := []rune(s)
	sort.Sort(sortRunes(r))
	return string(r)
}

func groupAnagrams(strs []string) [][]string {
	lookup := make(map[string][]string)
	for _, str := range strs {
		key := SortString(str)
		lookup[key] = append(lookup[key], str)
	}
	ret := make([][]string, 0)
	for _, v := range lookup {
		ret = append(ret, v)
	}
	return ret
}
