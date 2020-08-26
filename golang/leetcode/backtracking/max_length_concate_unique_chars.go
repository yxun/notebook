package backtracking

// 1239. Maximum Length of a Concatenated String with Unique Characters

// backtracking
func maxLength(arr []string) int {
	lookup := make([]int, 26)
	res := 0
	TrackMaxLength(arr, lookup, 0, &res, "")
	return res
}

func TrackMaxLength(arr []string, lookup []int, start int, res *int, str string) {
	if start == len(arr) {
		return
	}
	for i := start; i < len(arr); i++ {
		word := []rune(arr[i])
		isDuplicate := false
		for k := 0; k < len(word); k++ {
			c := word[k]
			if lookup[c-'a'] == 1 {
				for j := 0; j < k; j++ {
					lookup[word[j]-'a']--
				}
				isDuplicate = true
				break
			}
			lookup[c-'a']++
		}
		if !isDuplicate {
			*res = Max(*res, len(str)+len(word))
			TrackMaxLength(arr, lookup, start+1, res, str+string(word))
			for _, c := range word {
				lookup[c-'a']--
			}
		}
	}
}

func Max(x, y int) int {
	if x > y {
		return x
	}
	return y
}
