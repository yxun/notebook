package bfs

// 1236. Web Crawler
import "strings"

type HtmlParser struct{}

// bfs
func (p *HtmlParser) GetUrls(url string) []string {
	return []string{}
}

func crawl(startUrl string, htmlParser HtmlParser) []string {
	set := make(map[string]bool)
	queue := make([]string, 0)

	hostname := strings.Split(startUrl, "/")[2]
	queue = append(queue, startUrl)
	set[startUrl] = true

	for len(queue) != 0 {
		size := len(queue)
		for i := 0; i < size; i++ {
			currentUrl := queue[0]
			queue = queue[1:]
			for _, url := range htmlParser.GetUrls(currentUrl) {
				if strings.Contains(url, hostname) && !set[url] {
					queue = append(queue, url)
					set[url] = true
				}
			}
		}
	}
	res := make([]string, 0)
	for k := range set {
		res = append(res, k)
	}
	return res
}
