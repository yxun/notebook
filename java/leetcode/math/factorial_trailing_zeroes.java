/**
 * 172. Factorial Trailing Zeroes
 * Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
 */

public class factorial_trailing_zeroes {

    public int trailingZeroes(int n) {
        // count number of 5, N/5 + N/(5^2) + N/(5^3) + ...
        return n == 0 ? 0 : n / 5 + trailingZeroes(n / 5);

        // if find out the least significant bit of 1 in a binary number, count number of 2, N/2 + N/(2^2) + N/(2^3) + ...
    }
}