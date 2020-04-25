/**
 * 204. Count Primes
 * Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
 */

public class count_primes {

    public int countPrimes(int n) {
        // Sieve of Eratosthenes
        /**
         * To find all the prime numbers less than or equal to a given integer n by Eratosthenes' method:
         * Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
         * Initially, let p equal 2, the smallest prime number.
         * Enumerate the multiples of p by counting in increments of p from 2p to n, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
         * Find the first number greater than p in the list that is not marked. If there was no such number, stop. Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
         * When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
         * 
         * As a refinement, it is sufficient to mark the numbers in step 3 starting from p2, as all the smaller multiples of p will have already been marked at that point. This means that the algorithm is allowed to terminate in step 4 when p2 is greater than n.
         */

        boolean[] notPrimes = new boolean[n+1];
        int count = 0;
        for (int i = 2; i < n; i++) {
            if (notPrimes[i]) {
                continue;
            }
            count++;
            // starts from i*i
            for (long j = (long)(i)*i; j<n; j+=i) {
                notPrimes[(int)j] = true;
            }
        }        
        return count;
    }
}