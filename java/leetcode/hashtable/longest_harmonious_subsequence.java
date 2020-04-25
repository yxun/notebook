/**
 * 594. Longest Harmonious Subsequence
 * We define a harmounious array as an array where the difference between its maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence among all its possible subsequences.

Example 1:

Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
 */

import java.util.Map;
import java.util.HashMap;

public class longest_harmonious_subsequence {
    public int findLHS(int[] nums) {
        Map<Integer, Integer> countForNum = new HashMap<>();
        for (int num : nums) {
            countForNum.put(num, countForNum.getOrDefault(num, 0) + 1);
        }
        int longest = 0;
        for (int num : countForNum.keySet()) {
            if (countForNum.containsKey(num+1)) {
                longest = Math.max(longest, countForNum.get(num+1) + countForNum.get(num));
            }
        }
        return longest;
    }
}