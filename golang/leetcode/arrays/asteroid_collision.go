package arrays

// 735. Asteroid Collision

func asteroidCollision(asteroids []int) []int {
	// stack
	if len(asteroids) == 0 {
		return []int{}
	}

	stack := make([]int, 0)
	for i := 0; i < len(asteroids); i++ {
		// only need to resolve collisions under the following conditions
		// stack is non-empty and
		// currrent asteroid is negative and
		// top of the stack is positive and

		if len(stack) == 0 || asteroids[i] > 0 || stack[len(stack)-1] < 0 {
			// no collision
			stack = append(stack, asteroids[i])
		} else {
			/*
				// both are equal, destroy both
				if stack[len(stack)-1] == -asteroids[i] {
					stack = stack[:len(stack)-1]
					continue
				} else if stack[len(stack)-1] > -asteroids[i] {
					// stack top is larger
					continue
				} else {
					// stack top is smaller
					stack = stack[:len(stack)-1]
					i--
				}
			*/

			if stack[len(stack)-1] == -asteroids[i] {
				stack = stack[:len(stack)-1]
			} else if stack[len(stack)-1] < -asteroids[i] {
				stack = stack[:len(stack)-1]
				i--
			} else {
				continue
			}
		}
	}
	return stack
}
