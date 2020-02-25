
public class C3Strings {

    // Strings boot camp
    // A palindromic string is one which reads the same when it is reversed
    // time O(n), space O(1)
    public static boolean isPalindromic(String s) {
        for (int i = 0, j = s.length()-1; i < j; ++i, --j) {
            if (s.charAt(i) != s.charAt(j)) {
                return false;
            }
        }
        return true;
    }

    // Know your string libraries
    // Need to know both the String class as well as the StringBuilder class
    // Understand the implications of a string type which is immutable

    // The key methods on strings: charAt(1), compareTo("foo"), concat("bar"),
    // contains("aba"), endsWith("YZ"), indexOf("needle"), indexOf("needle", 12),
    // indexOf('A'), indexOf('B', offset), lastIndexOf("needle"), length(), replace('a', 'A'),
    // replace("a", "ABC"), "foo::bar::abc".split("::"), startsWith(prefix),
    // startsWith("www", "https://".length()), substring(1), substring(1,5),
    // toCharArray(), toLowerCase(), trim()

    // The key methods in StringBuilder: append(), charAt(), delete(), deleteCharAt(),
    // insert(), replace(), toString()

    // Interconvert Strings and Integers
    // you cannot use library functions like stoi in C++, parseInt in Java and int in Python
    // adding a digit to the beginning of a string is expensive, since all remaining digit have to be moved

    public static String intToString(int x) {
        boolean isNegative = false;
        if (x < 0) {
            isNegative = true;
        }

        StringBuilder s = new StringBuilder();
        do {
            s.append((char)('0' + Math.abs(x % 10)));
            x /= 10;
        } while (x != 0);

        if (isNegative) {
            s.append('-');  // Adds the negative sign back
        }
        s.reverse();
        return s.toString();
    }

    public static int stringToInt(String s) {
        int result = 0;
        for (int i = s.charAt(0) == '-' ? 1 : 0; i < s.length(); ++i) {
            final int digit = s.charAt(i) - '0';
            result = result * 10 + digit;
        }
        return s.charAt(0) == '-' ? -result : result;
    }

    // Base conversion
    // convert a string in base b1 to integer type using a sequence of multiple and adds
    // then convert that integer type to a string in base b2 using a sequence of modulus and division
    // time O(n(1 + logb2^b1))
    public static String convertBase(String numAsString, int b1, int b2) {
        boolean isNegative = numAsString.startsWith("-");
        int numAsInt = 0;
        for (int i = (isNegative ? 1 : 0); i < numAsString.length(); ++i) {
            numAsInt *= b1;
            numAsInt += Character.isDigit(numAsString.charAt(i)) 
                ? numAsString.charAt(i) - '0' 
                : numAsString.charAt(i) - 'A' + 10;
        }
        return (isNegative ? "-" : "") + (numAsInt == 0 ? "0" : constructFromBase(numAsInt, b2));
    }

    private static String constructFromBase(int numAsInt, int base) {
        return numAsInt == 0 
            ? "" 
            : constructFromBase(numAsInt / base, base) 
                + (char)(numAsInt % base >= 10 ? 'A' + numAsInt % base -10 
                                                : '0' + numAsInt % base);
    }

}