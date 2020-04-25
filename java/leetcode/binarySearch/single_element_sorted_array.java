/**
 * 540. Single Element in a Sorted Array
 * You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

 

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
 

Note: Your solution should run in O(log n) time and O(1) space.
 */


public class single_element_sorted_array {

    public int singleNonDuplicate(int[] nums) {
        int l = 0, h = nums.length - 1;
        while (l < h) {
            int m = l + (h-l) / 2;
            if (m % 2 == 1) {
                m--;  // make m be an even index
            }
            if (nums[m] == nums[m+1]) {
                l = m+2;
            } else {
                h = m;
            }
        }
        return nums[l];
    }

}