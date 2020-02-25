
import java.util.Map;
import java.util.HashMap;
import java.util.List;

public class C13DynamicProgramming {

    // DP is a general technique for solving optimization, search and counting problems that can be decomposed into subproblems.

    // Fibonacci numbers
    private static Map<Integer, Integer> cache = new HashMap<>();

    public static int fibonacci(int n) {
        if (n <= 1) {
            return n;
        } else if (!cache.containsKey(n)) {
            cache.put(n, fibonacci(n-2) + fibonacci(n-1));
        }
        return cache.get(n);
    }
    // time O(n), space O(n)

    // solution 2 iteratively fills in the cache in a bottom-up fashion
    public static int fibonacci2(int n ) {
        if (n <= 1) {
            return n;
        }

        int fMinus2 = 0;
        int fMinus1 = 1;
        for (int i = 2; i <= n; ++i) {
            int f = fMinus2 + fMinus1;
            fMinus2 = fMinus1;
            fMinus1 = f;
        }
        return fMinus1;
    }

    // find a way to break the problem into subproblems
    // the original problem can be solved relatively eaily once solutions to the subproblems are available
    // these subproblem solutions are cached

    // find the maximum sum over all subarrays of a given array of integer
    public static int findMaximumSubarray(List<Integer> A) {
        int minSum = 0, runningSum = 0, maxSum = 0;
        for (int i = 0; i < A.size(); ++i) {
            runningSum += A.get(i);
            if (runningSum < minSum) {
                minSum = runningSum;
            }
            if (runningSum - minSum > maxSum) {
                maxSum = runningSum - minSum;
            }
        }
        return maxSum;
    }

    // DP boot camp
    // Count the number of ways to traverse a 2D array
    // if i > 0 and j > 0, you can get to (i,j) from (i-1,j) or (j-1,i)
    public static int numberOfWays(int n, int m) {
        return computeNumberOfWaysToXY(n-1,m-1, new int[n][m]);
    }

    private static int computeNumberOfWaysToXY(int x, int y, int[][] numberOfWays) {
        if (x == 0 || y == 0) {
            return 1;
        }

        if (numberOfWays[x][y] == 0) {
            int waysTop = x == 0 ? 0 : computeNumberOfWaysToXY(x-1, y, numberOfWays);
            int waysLeft = x == 0 ? 0 : computeNumberOfWaysToXY(x, y-1, numberOfWays);
        }
        return numberOfWays[x][y];
    }
    // time O(nm), space O(nm)

    // Solution 2 math

}