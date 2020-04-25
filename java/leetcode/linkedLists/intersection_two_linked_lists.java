/**
 * 160. Intersection of Two Linked Lists
 * Write a program to find the node at which the intersection of two singly linked lists begins.
 * Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
 */

public class intersection_two_linked_lists {

    // length of list A = a + c, length of list B = b + c
    // a+c+b = b+c+a
    // when reach the tail of A, next to the head of B.
    // when reach the tail of B, next to the head of A.
    // if there is no intersaction, a+b = b+a, when l1 == l2 == null, exit

    public ListNode getIntersactionNode(ListNode headA, ListNode headB) {
        ListNode l1 = headA, l2 = headB;
        while (l1 != l2) {
            l1 = (l1 == null) ? headB : l1.next;
            l2 = (l2 == null) ? headA : l2.next;
        }
        return l1;
    }
}