package backtracking

// 17. Letter Combinations of a Phone Number
var (
	keys = []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
)

func letterCombinations(digits string) []string {
	combinations := make([]string, 0)
	if len(digits) == 0 {
		return combinations
	}
	prefix := make([]byte, 0)
	letterTrack(prefix, &combinations, digits)
	return combinations
}

func letterTrack(prefix []byte, combinations *[]string, digits string) {
	if len(prefix) == len(digits) {
		*combinations = append(*combinations, string(prefix))
		return
	}
	var curDigits int
	curDigits = int(digits[len(prefix)] - '0')
	letters := []byte(keys[curDigits])
	for _, c := range letters {
		prefix = append(prefix, c)
		letterTrack(prefix, combinations, digits)
		prefix = prefix[:len(prefix)-1]
	}
}
