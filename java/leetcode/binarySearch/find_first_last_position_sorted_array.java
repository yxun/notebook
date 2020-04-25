/**
 * 34. Find First and Last Position of Element in Sorted Array
 * Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
 */


public class find_first_last_position_sorted_array {

    public int[] searchRange(int[] nums, int target) {
        int first = findFirst(nums, target);
        int last = findFirst(nums, target+1)-1;
        if (first == nums.length || nums[first] != target) {
            return new int[]{-1,-1};
        } else {
            return new int[]{first, Math.max(first, last)};
        }
    }

    private int findFirst(int[] nums, int target) {
        int l = 0, h = nums.length;  // h is nums.length instead of nums.length-1
        while (l < h) {
            int m = l + (h-l) / 2;
            if (nums[m] >= target) {
                h = m;
            } else {
                l = m+1;
            }
        }
        return l;
    }
}