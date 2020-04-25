/**
 * 461. Hamming Distance
 * The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
 */

public class hamming_distance {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);

        /*
        int z = x ^ y;
        int cnt = 0;
        while (z != 0) {
            if ((z & 1) == 1) cnt++;
            z = z >> 1;
        }
        return cnt;
        */

        /*
        int z = x ^ y;
        int cnt = 0;
        while (z != 0) {
            z &= (z-1)
            cnt++;
        }
        return cnt;
        */
    }
}