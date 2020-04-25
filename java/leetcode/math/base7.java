/**
 * 504. Base 7
 * Given an integer, return its base 7 string representation.

Example 1:

Input: 100
Output: "202"
Example 2:

Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
 */

public class base7 {

    public String convertToBase7_1(int num) {
        if (num == 0) {
            return "0";
        }
        StringBuilder sb = new StringBuilder();
        boolean isNegative = num < 0;
        if (isNegative) {
            num = -num;
        }
        while (num > 0) {
            sb.append(num % 7);
            num /= 7;
        }
        String ret = sb.reverse().toString();
        return isNegative ? "-" + ret : ret;
    }

    public String convertToBase7_2(int num) {
        return Integer.toString(num, 7);
    }
}