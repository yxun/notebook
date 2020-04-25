/**
 * 485. Max Consecutive Ones
 * Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:

Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
 */
public class max_consecutive_ones {

    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0, cur = 0;
        for (int n : nums) {
            cur = n == 0 ? 0 : cur + 1;
            max = Math.max(max, cur);
        }
        return max;
    }
}