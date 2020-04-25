#%%
"""
- Merge k Sorted Lists
- https://leetcode.com/problems/merge-k-sorted-lists/
- Hard

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

#%%
class ListNode:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


#%%
class S:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        import heapq
        h = []
        for order, lst_head in enumerate(lists):
            if lst_head:
                heapq.heappush(h, (lst_head.val, order, lst_head))
        
        cur = ListNode(-1)
        dummy = cur
        while h:
            smallest_val, order, smallest_node = heapq.heappop(h)
            cur.next = smallest_node
            cur = cur.next
            if smallest_node.next:
                heapq.heappush(h, (smallest_node.next.val, order, smallest_node.next))
        
        return dummy.next


#%%
