/**
 * 
 */


public class gcd_lcm {

    public int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    public int gcd_bitwise(int a, int b) {
        if (a < b) {
            return gcd_bitwise(b, a);
        }
        if (b == 0) {
            return a;
        }

        boolean isAEven = isEven(a), isBEven = isEven(b);
        if (isAEven && isBEven) {
            return 2 * gcd_bitwise(a >> 1, b >> 1);
        } else if (isAEven && !isBEven) {
            return gcd_bitwise(a >> 1, b);
        } else if (!isAEven && isBEven) {
            return gcd_bitwise(a, b >> 1);
        } else {
            return gcd_bitwise(b, a-b);
        }
    }
}

