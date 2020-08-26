package arrays

// 1375. Bulb Switcher III

// right is the number of right most lighted bulb
// iterate the input light A, update right = max(right, A[i])
// now we have lighted i+1 bulbs, if right == i+1, all the previous bulbs(to the left) are turned on
// prove with contradiction : right > i+1 , there must be a bulb is off between 1 to right from total i+1 turned on bulbs

// time O(N), space O(1)
func numTimesAllBlue(light []int) int {
	right := 0
	res := 0
	for i := 0; i < len(light); i++ {
		right = Max(right, light[i])
		if right == i+1 {
			res++
		}
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
