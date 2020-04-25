#%%
"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

#%%
## 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head == None or head.next == None: return head
        if m >= n: return head

        cur = head
        pre = head
        
        for i in range(0, m-1):
            pre = cur
            cur = cur.next

        left = pre
        start = cur

        # reverse
        for i in range(m, n+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        if start != head:
            left.next = pre
        else:
            head = pre

        start.next = cur

        return head

#%%
"""
doctest

1->2->3->4->5->6->7->8->9

m = 2, n = 5

1->5->4->3->2->6->7->8->9

left = 1
start = 2
cur = 2

i = 2
nxt = 3
cur.next = 1
pre = 2
cur = 3
1<->2 3...

i = 3
nxt = 4
cur.next = 2
pre = 3
cur = 4
1<->2<-3 4

i = 4
nxt = 5
cur.next = 3
pre = 4
cur = 5
1<->2<-3<-4 5

i =5
1<->2<-3<-4<-5 6
cur = 6


1->
6<-2<-3<-4<-5<-1
=====

1->2->3->4->5->6->7->8->9

m = 1, n = 5

5->4->3->2->1->6->7->8->9

left , start = 1,1 


3->5
m=1 n=2

left = 3
start = 3

i 1, 2

i = 1
nxt = 5
cur.next = 3
pre = 3
cur = 5

3 5

i = 2
nxt = None
cur.next = 3
pre = 5
cur = None
3<-5

None<-3<-
"""
