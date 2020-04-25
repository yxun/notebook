#%%
"""
- Reverse Nodes in k-group
- https://leetcode.com/problems/reverse-nodes-in-k-group/
- Hard

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

#%%
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

#%%
class S:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        cnt, pre, cur, nex = 1, None, head, head.next
        p = head
        while p:
            cnt += 1
            p = p.next
        
        if cnt-1 >= k:
            cnt = 1
            while cnt < k and nex:
                cnt += 1
                cur.next = pre
                pre = cur
                cur = nex
                nex = nex.next
            
            cur.next = pre
        else:
            return cur
        
        if nex:
            head.next = self.reverseKGroup(nex, k)
        
        return cur


#%%
