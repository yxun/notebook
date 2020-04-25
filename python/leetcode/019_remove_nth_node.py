#%%
'''
- Remove Nth Node from End of List
- https://leetcode.com/problems/remove-nth-node-from-end-of-list/
- Medium

Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
'''

#%%
class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

#%%
# Use two points

class S:
    def removeNthFromEnd(slef, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        dummy = ListNode(-1)
        dummy.next = head
        p, q = dummy, dummy

        for i in range(n):
            q = q.next
        
        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next
        return dummy.next

#%%

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

s = S()
head = n1
n = 2


res = s.removeNthFromEnd(head, n)

while res:
    print(res.data)
    res = res.next


#%%
