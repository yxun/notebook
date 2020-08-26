package arrays

// 1488. Avoid Flood in The City

func avoidFlood(rains []int) []int {
	res := make([]int, len(rains))
	fulllakes := make(map[int]int) // lake number -> day on which it became full
	drydays := make(map[int]bool)  // list of avaiable days that can be used for drying a full lake

	for i := 0; i < len(rains); i++ {
		if rains[i] == 0 {
			drydays[i] = true
			res[i] = 1 // This willl get overwritten
		} else {
			if day, ok := fulllakes[rains[i]]; ok {
				// already full
				dday := findDrydays(day, &drydays)
				if dday == -1 {
					return []int{}
				}
				res[dday] = rains[i]
				delete(drydays, dday)
			}
			fulllakes[rains[i]] = i
			res[i] = -1
		}
	}
	return res
}

func findDrydays(day int, drydays *map[int]bool) int {
	for d := range *drydays {
		if d > day {
			return d
		}
	}
	return -1
}
