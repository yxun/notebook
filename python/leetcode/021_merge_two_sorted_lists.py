#%%
'''
- Merge Two Sorted Lists
- https://leetcode.com/problems/merge-two-sorted-lists/
- Easy

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''

#%%
#%%
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

#%%
class S:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        dummy = ListNode(-1)
        cur = dummy

        while l1 and l2:
            if l1.data < l2.data:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
            
        return dummy.next
