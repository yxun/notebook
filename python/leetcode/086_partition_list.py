#%%
"""
- Partition List
- https://leetcode.com/problems/partition-list/
- Medium

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

#%%
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#%%
class S1:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head or head.next == None: return head

        cur = ListNode(-1)
        cur.next = head
        l1, g1 = ListNode(-1), ListNode(-1)
        l2, g2 = l1, g1

        while cur.next:
            nex = cur.next
            if nex.val < x:
                l2.next = nex
                l2 = l2.next
            else:
                g2.next = nex
                g2 = g2.next
            cur = cur.next
        
        g2.next = None
        l2.next = g1.next
        return l1.next
