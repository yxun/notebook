#%%
"""
- Remove Duplicates from Sorted List II
- https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
- Medium

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
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
        if not head or head.next == None: return head
        
        pre, cur = None, head
        duplicate = False
        while cur.next:
            if cur.val != cur.next.val and not duplicate:
                pre = cur
                cur = cur.next
            elif cur.val == cur.next.val:
                duplicate = True
                cur = cur.next
                if cur.next == None and pre != None:
                    pre.next = None
                    
                elif cur.next == None and pre == None:
                    return None    
            
            elif duplicate and cur.val != cur.next.val:
                if pre == None:
                    head = cur.next
                else:
                    pre.next = cur.next
                cur = cur.next
                duplicate = False
        
        return head
        