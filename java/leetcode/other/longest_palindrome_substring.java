/**
 * 5. Longest Palindromic Substring
 * Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
 */

public class longest_palindrome_substring {
    // O(n^2)
    public String longestPalindrome(String s) {
        if (s.length() == 0) {
             return s;
        }

        int curLen = 0;
        int start = -1;
        char[] array = s.toCharArray();
        for (int i = 0; i < array.length; i++) {
            if (isPalindrome(array, i-curLen-1, i)) {
                start = i - curLen - 1;
                curLen += 2;
            } else if (isPalindrome(array, i-curLen, i)) {
                start = i - curLen;
                curLen += 1;
            }
        }
        return new String(array, start, curLen);
    }

    private boolean isPalindrome(char[] array, int start, int end) {
        if (start < 0) {
            return false;
        }

        while (start < end) {
            if (array[start++] != array[end--]) {
                return false;
            }
        }
        return true;
    }
}