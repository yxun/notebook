#%%
"""
- Remove Duplicates from Sorted List
- https://leetcode.com/problems/remove-duplicates-from-sorted-list/
- Easy

Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#%%
##
class S1:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or head.next == None:
            return head

        pre, cur = head, head
        duplicate = False
        while cur.next:
            if cur.val != cur.next.val and not duplicate:
                cur = cur.next
            elif cur.val == cur.next.val:
                if not duplicate:
                    pre = cur
                duplicate = True
                cur = cur.next
                if cur.next == None:
                    pre.next = None
            elif duplicate and cur.val != cur.next.val:
                pre.next = cur.next
                duplicate = False
        
        return head

#%%
class S2:
    def deleteDuplicates(self, head):
        dummy = head
        while head:
            while head.next and head.next.val == head.val:
                head.next = head.next.next
            head = head.next
        return dummy
