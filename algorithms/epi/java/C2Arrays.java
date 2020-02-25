
import java.util.Collections;
import java.util.List;

public class C2Arrays {

    // Array boot camp
    // When working with arrays you should take advantage of the fact that you can operate efficiently on both ends
    // partition the array into three subarrays: Even, Unclassified, and Odd
    // time O(n), space O(1)
    public static void evenOdd(int[] A) {
        int nextEven = 0, nextOdd = A.length - 1;
        while (nextEven < nextOdd) {
            if (A[nextEven] % 2 == 0) {
                nextEven++;
            } else {
                int temp = A[nextEven];
                A[nextEven] = A[nextOdd];
                A[nextOdd--] = temp;
            }
        }
    }

    /** Know array libraries
     * The basic array type in Java is fixed-size
     * The ArrayList type implements a dynamically resized array
     * Know the syntax for allocating and initializing an array, i.e. new int[]{1,2,3}
     * Understand how to instantiate a 2D array, e.g. new Integer[3][] creates an array which will hold three rows, each of these must be explicitly assigned
     * Don't forget the length of an array is given by the length field, unlike Collections, which uses the size() method, and String, which use the length() method
     * The Arrays class consists of a set of static utility methods: 
     * asList(), binarySearch(A, 641), copyOf(A), copyOfRange(A, 1, 5), equals(A, B), fill(A, 42), find(A, 28), sort(A), sort(A, cmp), toString()
     * Understand the variants of these methods, e.g. how to create a copy of a subarray.
     * Understand what "deep" means when checking equality of arrays, and hashing them
     */

    // The Dutch national flag problem
    // trivial O(n) space and O(n^2) time, two passes
    
    // space O(1), time O(n)
    public static enum Color { RED, WHITE, BLUE }

    public static void  dutchFlagPartition01(int pivotIndex, List<Color> A) {
        Color pivot = A.get(pivotIndex);
        // First pass: group elements smaller than pivot
        for (int i = 0; i < A.size(); ++i) {
            // Look for a smaller element
            for (int j = i+1; j < A.size(); ++j) {
                if (A.get(j).ordinal() < pivot.ordinal()) {
                    Collections.swap(A, i, j);
                    break;
                }
            }
        }

        // Second pass: group elements larger than pivot
        for (int i = A.size()-1; i >= 0 && A.get(i).ordinal() >= pivot.ordinal(); --i) {
            // Look for a larger element. Stop when we reach an element less
            // than pivot, since first pass has moved them to the start of A
            for (int j = i-1; j >= 0 && A.get(j).ordinal() >= pivot.ordinal(); --j) {
                if (A.get(j).ordinal() > pivot.ordinal()) {
                    Collections.swap(A, i, j);
                    break;
                }
            }
        }
    }

    // time O(n), space O(1)
    public static void dutchFlagPartition02(int pivotIndex, List<Color> A) {
        Color pivot = A.get(pivotIndex);
        // First pass: group elements smaller than pivot
        int smaller = 0;
        for (int i = 0; i < A.size(); ++i) {
            if (A.get(i).ordinal() < pivot.ordinal()) {
                Collections.swap(A, smaller++, i);
            }
        }

        // Second pass: group elements larger than pivot
        int larger = A.size() - 1;
        for (int i = A.size()-1; i >= 0 && A.get(i).ordinal() >= pivot.ordinal(); --i) {
            if (A.get(i).ordinal() > pivot.ordinal()) {
                Collections.swap(A, larger--, i);
            }
        }
    }

    // one pass, four subarrays: less than pivot, equal to pivot, unclassified and greater than pivot
    public static void dutchFlagPartition03(int pivotIndex, List<Color> A) {
        Color pivot = A.get(pivotIndex);
        /**
         * Keep the following invariants during partitioning:
         * bottom group: A.subList(0, smaller)
         * middle group: A.subLst(smaller, equal)
         * unclassified group: A.subList(equal, larger)
         * top group: A.subList(larger, A.size())
         */
        int smaller = 0, equal = 0, larger = A.size();

        // Keep iterating as long as there is an unclassified element
        while (equal < larger) {
            // A.get(equal) is the incoming unclassified element
            if (A.get(equal).ordinal() < pivot.ordinal()) {
                Collections.swap(A, smaller++, equal++);
            } else if (A.get(equal).ordinal() == pivot.ordinal()) {
                ++equal;
            } else {
                // A.get(equal) > pivot
                Collections.swap(A, equal, --larger);
            }
        }
    }

}