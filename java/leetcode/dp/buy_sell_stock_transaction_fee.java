/**
 * 714. Best Time to Buy and Sell Stock with Transaction Fee
 * Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.

You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction. You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)

Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1
Selling at prices[3] = 8
Buying at prices[4] = 4
Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
 */

public class buy_sell_stock_transaction_fee {

    public int maxProfit(int[] prices, int fee) {
        int N = prices.length;
        int[] buy = new int[N];
        int[] s1 = new int[N];
        int[] sell = new int[N];
        int[] s2 = new int[N];
        s1[0] = buy[0] = -prices[0];
        sell[0] = s2[0] = 0;
        for (int i = 1; i < N; i++) {
            buy[i] = Math.max(sell[i-1], s2[i-1]) - prices[i];
            s1[i] = Math.max(buy[i-1], s1[i-1]);
            sell[i] = Math.max(buy[i-1], s1[i-1]) - fee + prices[i];
            s2[i] = Math.max(s2[i-1], sell[i-1]);
        }
        return Math.max(sell[N-1], s2[N-1]);
    }
}