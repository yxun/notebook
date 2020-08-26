package tree

// 96. Unique Binary Search Trees

// dp
// enumerate number i in the sequence, use it as the root
// 1..(i-1) lay on the left branch of the root
// (i+1)..n lay on the right branch of the root
// construct the subtree recursively
// G(n) number of unique BST of length n
// F(i, n), the number of unique BST, where i is the root and sequence ranges from 1 to n
// G(n) = F(1, n) + F(2, n) + ... F(n,n)
// G(0) = 1, G(1) = 1
// F(i, n) = G(i-1) * G(n-i)
// G(n) = G(0)*G(n-1) + G(1)*G(n-2) ... G(n-1)G(0)

func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0], dp[1] = 1, 1
	for i := 2; i <= n; i++ {
		for j := 1; j <= i; j++ {
			dp[i] += dp[j-1] * dp[i-j]
		}
	}
	return dp[n]
}
