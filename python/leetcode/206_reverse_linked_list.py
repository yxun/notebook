#%%
"""
- Reverse Linked List
- https://leetcode.com/problems/reverse-linked-list/
- Easy

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#%%
class S1:
    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        return pre

#%%
class S2:
    def reverseList(self, head):
        if not head: return head

        pre = None
        while head.next:
            tmp = head.next
            head.next = pre
            pre = head
            head = tmp
        head.next = pre
        return head

#%%
class S3:
    def reverseList(self, head):
        def reverseHelper(head, new_head):
            if not head: return new_head

            nex = head.next
            head.next = new_head
            return reverseHelper(nex, head)

        return reverseHelper(head, None)
        