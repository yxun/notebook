package dfs

// 733. Flood Fill

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	directions := [][]int{{0, 1}, {0, -1}, {1, 0}, {-1, 0}}
	if image[sr][sc] != newColor {
		dfsFill(image, sr, sc, image[sr][sc], newColor, directions)
	}
	return image
}

func dfsFill(image [][]int, sr int, sc int, color int, newColor int, directions [][]int) {
	if sr < 0 || sc < 0 || sr >= len(image) || sc >= len(image[0]) || image[sr][sc] != color {
		return
	}
	image[sr][sc] = newColor
	for _, d := range directions {
		dfsFill(image, sr+d[0], sc+d[1], color, newColor, directions)
	}
}
