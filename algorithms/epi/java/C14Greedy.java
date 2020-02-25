

public class C14Greedy {

    // Greedy boot camp
    // making change results in the minimum number of coins
    public static int changeMaking(int cents) {
        final int[] COINS = {100, 50, 25, 10, 5, 1};
        int numCoins = 0;
        for (int i = 0; i < COINS.length; i++) {
            numCoins += cents / COINS[i];
            cents %= COINS[i];
        }
        return numCoins;
    }

    // A greedy algorithm is often the right choice for an optimization problem where there is a natural set of choices to select from
}