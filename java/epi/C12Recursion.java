import java.util.List;
import java.util.ArrayList;

public class C12Recursion {

    // A recursive function consists of base cases and calls to the same function with different arguments
    // Both backtracking and branch-and-bound are naturally formulated using recursion

    // Recursion boot camp
    // The Euclidean algorithm for calculating the greatest common divisor (GCD)
    public static long GCD(long x, long y) { return y == 0 ? x : GCD(y, x % y); }
    // time O(logmax(x,y))

    // Use recursion as alternative to deeply nested iteration loops
    // If you are asked to remove recursion, consider mimicking call stack with the stack data structure
    // If a recursive function may end up being called with the same arguments more than once, cache the results (Dynamic Programming)

    // recursive divide-and-conquer, triomino
    
    // Generate the power set
    // there are 2^n subsets of a given set S of size n. There are 2^k k-bit words
    // bruce-force
    public static List<List<Integer>> generatePowerSet(List<Integer> inputSet) {
        List<List<Integer>> powerSet = new ArrayList<>();
        directedPowerSet(inputSet, 0, new ArrayList<Integer>(), powerSet);
        return powerSet;
    }

    // Generate all subsets whose intersection with inputSet[0],...
    // inputSet[toBeSelected-1] is exactly selectedSoFar
    private static void directedPowerSet(List<Integer> inputSet, int toBeSelected, 
                                        List<Integer> selectedSoFar, List<List<Integer>> powerSet) {
        
        if (toBeSelected == inputSet.size()) {
            powerSet.add(new ArrayList<>(selectedSoFar));
            return;
        }
        // Generate all subsets that contain inputSet[toBeSelected]
        selectedSoFar.add(inputSet.get(toBeSelected));
        directedPowerSet(inputSet, toBeSelected+1, selectedSoFar, powerSet);
        // Generate all subsets that do not contain inputSet[toBeSelected]
        selectedSoFar.remove(selectedSoFar.size()-1);
        directedPowerSet(inputSet, toBeSelected+1, selectedSoFar, powerSet);  
    }
    // time C(n) = 2C(n-1), C(n) = O(2^n), O(n2^n), space O(n2^n)
}