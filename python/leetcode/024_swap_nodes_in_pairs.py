#%%
"""
- Swap Nodes in Pairs
- https://leetcode.com/problems/swap-nodes-in-pairs/
- Medium

Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

#%%
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

#%%
class S1:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or not head.next:
            return head
        
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
   

#%%
class S2:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        cur = dummy

        while cur.next and cur.next.next:
            next_one, next_two, next_three = cur.next, cur.next.next, cur.next.next.next
            cur.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            cur = next_one
        return dummy.next
        