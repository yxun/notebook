

public class knapsack {

    // item i , volume w and value v
    // put item i into pack, dp[i][j] = dp[i-1][j-W] + v
    // not put item i, dp[i][j] = dp[i-1][j]
    // dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

    public int knapsack(int W, int N, int[] weights, int[] values) {
        int[][] dp = new int[N+1][W+1];
        for (int i = 1; i <= N; i++) {
            int w = weights[i-1], v = values[i-1];
            for (int j = 1; j <= W; j++) {
                if (j >= w) {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-w]+v);
                } else {
                    dp[i][j] = dp[i-1][j];
                }
            }
        }
        return dp[N][W];
    }

    // space optimization
    // dp[j] = max(dp[j], dp[j-w] + v)

    public int knapsack2(int W, int N, int[] weights, int[] values) {
        int[] dp = new int[W+1];
        for (int i = 1; i <= N; i++) {
            int w = weights[i-1], v = values[i-1];
            for (int j = W; j >= 1; j--) {
                if (j >= w) {
                    dp[j] = Math.max(dp[j], dp[j-w] + v);
                }
            }
        }
        return dp[W];
    }

}