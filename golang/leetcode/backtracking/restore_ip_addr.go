package backtracking

// 93. Restore IP Addresses
import (
	"strconv"
)

func restoreIpAddresses(s string) []string {
	addresses := make([]string, 0)
	var temp []byte
	ipAddrTrack(0, temp, &addresses, s)
	return addresses
}

func ipAddrTrack(k int, temp []byte, addresses *[]string, s string) {
	if k == 4 || len(s) == 0 {
		if k == 4 && len(s) == 0 {
			*addresses = append(*addresses, string(temp))
		}
		return
	}
	for i := 0; i < len(s) && i <= 2; i++ {
		if i != 0 && s[0] == '0' {
			break
		}
		part := s[0 : i+1]
		num, _ := strconv.Atoi(part)
		if num <= 255 {
			if len(temp) != 0 {
				part = "." + part
			}
			temp = append(temp, []byte(part)...)
			ipAddrTrack(k+1, temp, addresses, s[i+1:])
			temp = temp[:len(temp)-len(part)]
		}
	}
}
