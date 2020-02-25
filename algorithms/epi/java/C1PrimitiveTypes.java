
public class C1PrimitiveTypes {

    // Primitive types boot camp
    public static short countBits(int x) {
        short numBits = 0;
        while (x != 0) {
            numBits += (x & 1);
            x >>>= 1;
        }
        return numBits;
    }

    /**
    * In Java an int is always 32 bits
    * Understand the difference between box-types (Integer, Double, etc.) and primitive types
    * Be comfortable with the bitwise operations, particularly XOR
    * Understand how to use masks and create them in an machine independent way
    * Know fast ways to clear the lowermost set bit
    * Understand signedness and its implications to shifting
    * Consider using a cache
    * Be aware that commutativity and associativity
    * Know the constants denoting the maximum and minimum values, 
    * e.g. Integer.MIN_VALUE, Float.MAX_VALUE, Double.SIZE, Boolean.TRUE
    * Know the box-types, especially the factories,
    * e.g. Double.valueOf("1.23"), Boolean.valueOf(true), Integer.parseInt("42"), Float.toString(-1.23)
    * Understand the limits of autoboxing
    * Konw how to interconvert integers, characters, and strings
    * e.g. Character.getNumbericValue(x) (or just x - '0'), String.valueOf(123)
    * The key methods in Math: abs(), ceil(), floor(), min(), max(), pow(), sqrt()
    * The key methods in Random: nextInt(), nextBoolean(), nextDouble()
    */

    // Computing the parity of a word
    // The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0
    
    // the brute-force, time O(n)
    public static short parity1(long x) {
        short result = 0;
        while (x != 0) {
            result ^= (x & 1);
            x >>>= 1;
        }
        return result;
    }

    /** get the lowest set bit of x
     * y = x & ~(x-1)
     * e.g. x = 00101100 , y = 00101100 & 11010100 = 00000100
     * Time complexity O(s), where s is the number of bits set to 1 in x
     */

    public static short parity2(long x) {
        short result = 0;
        while (x != 0) {
            result ^= 1;
            x &= (x-1);  // Drops the lowest set bit of x
        }
        return result;
    }

    // caching, grouping 64 bit long integer into four nonoverlapping 16 bit subwords
    /*
    public static short parity3(long x) {
        final int MASK_SIZE = 16;
        final int BIT_MASK = 0xFFFF;
        return (short) (
            precomputedParity[(int)((x >>> (3 * MASK_SIZE)) & BIT_MASK)]
            ^ precomputedParity[(int)((x >>> (2 * MASK_SIZE)) & BIT_MASK)]
            ^ precomputedParity[(int)((x >>> MASK_SIZE) & BIT_MASK)]
            ^ precomputedParity[(int)(x & BIT_MASK)]
        );
    }
    */
    // time O(logn), where n is the word size
    public static short parity3(long x) {
        x ^= x >>> 32;
        x ^= x >>> 16;
        x ^= x >>> 8;
        x ^= x >>> 4;
        x ^= x >>> 2;
        x ^= x >>> 1;
        return (short)(x & 0x1);
    }

    /** Variant
     * Right propagate the rightmost set bit in x, e.g. 01010000 to 01011111
     * Compute x modulo a power of two, e.g. returns 13 for 77 mod 64
     * Test if x is power of 2
     */

}
